from django.core.management.base import BaseCommand

from artd_location.data.chile_regions import CHILE_REGIONS
from artd_location.models import Country, Region


class Command(BaseCommand):
    help = "Create regions of Chile"

    def handle(self, *args, **kwargs):
        country = Country.objects.get(id=41)
        for region in CHILE_REGIONS:
            if Region.objects.filter(id=region[0]).count() == 0:
                Region.objects.create(
                    id=region[0],
                    name=region[2],
                    code=region[1],
                    country=country,
                )
                self.stdout.write(self.style.SUCCESS(f"{region[1]} was created"))
            else:
                region_obj = Region.objects.get(
                    id=region[0],
                )
                region_obj.name = region[2]
                region_obj.code = region[1]
                region_obj.country = country
                region_obj.save()
                self.stdout.write(self.style.WARNING(f"{region[1]} was updated"))
