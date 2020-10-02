from django.core.management.base import BaseCommand, CommandError
from api.models import Manufacturer, ShoeColor, ShoeType, Shoe

# Got help from Detrich Schilling here in study hall/ the Django documentation.
# https://docs.djangoproject.com/en/3.0/howto/custom-management-commands/
class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        shoetype_datagroup = ['sneaker', 'boot', 'sandal', 'dress', 'other']
        for data in shoetype_datagroup:
            ShoeType.objects.create(style=data)
        shoecolor_datagroup = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet', 'White', 'Black']
        for data in shoecolor_datagroup:
            ShoeColor.objects.create(color_name=data)