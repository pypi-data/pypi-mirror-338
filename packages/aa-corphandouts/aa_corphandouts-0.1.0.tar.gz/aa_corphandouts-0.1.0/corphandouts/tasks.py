"""Tasks."""

from collections import Counter

from celery import group, shared_task
from corptools.models import CorpAsset

from eveuniverse.models import EveType

from allianceauth.services.hooks import get_extension_logger

from corphandouts.corptools import (
    get_assets_corporation_division,
    get_ship_fit,
    update_corp_item_names_bulk,
)
from corphandouts.esi import get_corporation_asset_names
from corphandouts.models import (
    DoctrineReport,
    FittingCorrection,
    FittingReport,
    FittingToCorrect,
)

logger = get_extension_logger(__name__)


@shared_task()
def update_doctrine_report(doctrine_report_id: int):
    """
    Goes through corporation assets to check what fits need to be updated
    """
    logger.info("Updating doctrine report id %d", doctrine_report_id)
    doctrine_report = DoctrineReport.objects.get(id=doctrine_report_id)
    assets_in_corporation_division = get_assets_corporation_division(
        doctrine_report.corporation,
        doctrine_report.location,
        doctrine_report.corporation_hangar_division,
    )
    logger.debug(
        "%d assets fetched in the corporation division",
        assets_in_corporation_division.count(),
    )

    tasks = []
    for fitting_to_check in doctrine_report.fittings.all():
        fit_ship_type_id = fitting_to_check.fit.ship_type_type_id
        item_ids_to_check = assets_in_corporation_division.filter(
            type_id=fit_ship_type_id
        ).values_list("item_id", flat=True)
        logger.debug(
            "%d item with type id %d found %s",
            item_ids_to_check.count(),
            fit_ship_type_id,
            list(item_ids_to_check),
        )
        tasks.append(
            check_doctrine_fit.si(fitting_to_check.id, list(item_ids_to_check))
        )

    group(tasks).delay()


@shared_task()
def check_doctrine_fit(fitting_report_id: int, ships_item_ids: list[int]):
    """
    Receives a list of item_ids that are in the hangar appropriate for this fitting and checks which of them are fitted correctly
    """
    logger.info("Updating fitting report id %d", fitting_report_id)
    logger.debug(ships_item_ids)
    fitting_report = FittingReport.objects.get(id=fitting_report_id)

    expected_fitting_items = fitting_report.fit.items.all()
    expected_fitting_counter = Counter(
        expected_fitting_items.filter(
            flag__regex=r"^(Hi|Med|Lo|Rig|SubSystem)Slot\d$"
        ).values_list("type_id", flat=True)
    )
    expected_cargo_counter = Counter(
        expected_fitting_items.filter(flag="Cargo").values_list("type_id", flat=True)
    )
    logger.debug(expected_fitting_counter)
    logger.debug(expected_cargo_counter)

    fit_ok_count = 0
    fits_to_fix = []

    for ships_item_id in ships_item_ids:
        logger.debug("Checking item id %d", ships_item_id)

        # Deletes existing corrections if any to overwrite
        FittingToCorrect.objects.filter(item__item_id=ships_item_id).delete()

        current_ship_items = get_ship_fit(ships_item_id)
        current_fitting_counter = Counter(
            current_ship_items.filter(
                location_flag__regex=r"^(Hi|Med|Lo|Rig|SubSystem)Slot\d$"
            ).values_list("type_id", flat=True)
        )
        current_cargo_counter = Counter(
            current_ship_items.filter(location_flag="Cargo").values_list(
                "type_id", flat=True
            )
        )
        current_fitting_counter.subtract(expected_fitting_counter)
        current_cargo_counter.subtract(expected_cargo_counter)
        logger.debug(current_fitting_counter)
        logger.debug(current_cargo_counter)

        if all(current_fitting_counter.values()) and all(
            current_cargo_counter.values()
        ):
            logger.debug("%d fit is correct", ships_item_id)
            fit_ok_count += 1

        else:
            logger.info("%d fit is incorrect", ships_item_id)
            fits_to_fix.append(
                (ships_item_id, current_fitting_counter, current_cargo_counter)
            )

    if not fits_to_fix:
        return
    ships_to_fix_item_ids = [fit[0] for fit in fits_to_fix]
    populate_ships_names(
        fitting_report.doctrine.corporation.corporation.corporation_id,
        ships_to_fix_item_ids,
    )

    # TODO split in tasks
    for item_type_id, fitting_difference, cargo_difference in fits_to_fix:
        corp_asset = CorpAsset.objects.get(item_id=item_type_id)
        fitting_to_correct = FittingToCorrect.objects.create(
            fit=fitting_report, item=corp_asset
        )
        corrections = []
        for type_id, amount in fitting_difference.items():
            if amount:
                amount = -amount
                eve_type, _ = EveType.objects.get_or_create_esi(id=type_id)
                corrections.append(
                    FittingCorrection(
                        fit_to_correct=fitting_to_correct,
                        eve_type=eve_type,
                        correction=amount,
                        correction_type=FittingCorrection.CorrectionType.FITTING,
                    )
                )
        for type_id, amount in cargo_difference.items():
            if amount:
                amount = -amount
                eve_type, _ = EveType.objects.get_or_create_esi(id=type_id)
                corrections.append(
                    FittingCorrection(
                        fit_to_correct=fitting_to_correct,
                        eve_type=eve_type,
                        correction=amount,
                        correction_type=FittingCorrection.CorrectionType.CARGO,
                    )
                )

        logger.debug(corrections)
        FittingCorrection.objects.bulk_create(corrections)


def populate_ships_names(corporation_id: int, ships_items_ids: list[int]):
    """
    Queries the name of all these items from the ESI and populates them in corptools
    """
    item_names = get_corporation_asset_names(corporation_id, ships_items_ids)
    logger.debug(item_names)
    update_corp_item_names_bulk(item_names)
