from django.core.management.base import BaseCommand

from artd_location.data.chile_cities import CITIES
from artd_location.models import City, Region


class Command(BaseCommand):
    help = "Create cities in Chile"

    def handle(self, *args, **kwargs):
        for city in CITIES:
            region = Region.objects.get(id=city[1])
            name: str = city[3]
            name = name.title()
            name_in_capital_letters: str = city[4]
            name_in_capital_letters = name_in_capital_letters.upper()
            if City.objects.filter(id=city[0]).count() == 0:
                City.objects.create(
                    id=city[0],
                    name=name,
                    name_in_capital_letters=name_in_capital_letters,
                    code=city[2],
                    region=region,
                )
                self.stdout.write(self.style.SUCCESS(f"{city[3]} was created"))
            else:
                city_obj = City.objects.get(
                    id=city[0],
                )
                city_obj.name = name
                city_obj.name_in_capital_letters = name_in_capital_letters
                city_obj.code = city[2]
                city_obj.region = region
                city_obj.save()
                self.stdout.write(self.style.WARNING(f"{city[3]} was updated"))
