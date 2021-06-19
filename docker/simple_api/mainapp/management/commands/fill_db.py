from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from mainapp.models import POI
import json


class Command(BaseCommand):
    help = 'Fill db'

    def handle(self, *args, **options):
        # CREATE SU
        User.objects.all().delete()
        User.objects.create_superuser('user', 'mail@mail.ru', '1234567890')

        # CREATE POIS
        POI.objects.all().delete()
        with open(r'/var/www/data.json', 'r') as fh:
            all_pois = json.load(fh)

        for i, poi in enumerate(all_pois):
            new_poi = POI(i+1, poi)
            new_poi.save()
