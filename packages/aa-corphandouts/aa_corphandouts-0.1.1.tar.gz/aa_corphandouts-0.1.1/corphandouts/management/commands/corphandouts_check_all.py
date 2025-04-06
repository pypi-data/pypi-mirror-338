from django.core.management.base import BaseCommand

from corphandouts.tasks import update_all_doctrines


class Command(BaseCommand):

    def handle(self, *args, **options):
        update_all_doctrines()
