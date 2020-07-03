from django.core.management.base import BaseCommand
from django.conf import settings
from json_api.models import User, ActivityPeriod

class Command(BaseCommand):
    help = 'Deletes all data from DB'

    def handle(self, *args, **kwargs):
        ActivityPeriod.objects.all().delete()
        User.objects.all().delete()
        print('Deleted all data successfully')
