import NationsInnDb.Db.Dbupdater as dbu
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "scrape"

    def handle(self, *args, **options):

        dbu.Dbupdater()
