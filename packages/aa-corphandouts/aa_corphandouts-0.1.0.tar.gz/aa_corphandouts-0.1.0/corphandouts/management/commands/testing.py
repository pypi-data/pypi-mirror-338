from django.core.management.base import BaseCommand

from corphandouts.tasks import update_doctrine_report


class Command(BaseCommand):

    def handle(self, *args, **options):
        update_doctrine_report(1)
