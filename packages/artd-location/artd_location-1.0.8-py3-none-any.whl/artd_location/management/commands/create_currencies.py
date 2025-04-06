import json
from django.core.management.base import BaseCommand
from artd_location.models import Currency, Country
from artd_location.data.currencies import CURRENCIES


class Command(BaseCommand):
    help = "Populates the database with Latin American currencies"

    def handle(self, *args, **kwargs):
        try:
            for currency_data in CURRENCIES:
                country = Country.objects.get(id=currency_data["country"])
                if not country:
                    self.stderr.write(
                        self.style.ERROR(
                            f"Country with ID {currency_data['country']} does not exist."
                        )
                    )
                    continue
                Currency.objects.update_or_create(
                    code=currency_data["code"],
                    defaults={
                        "name": currency_data["name"],
                        "symbol": currency_data["symbol"],
                        "country": country,
                    },
                )

            self.stdout.write(
                self.style.SUCCESS("Currencies have been successfully added.")
            )
        except FileNotFoundError:
            self.stderr.write(
                self.style.ERROR("The file 'currencies.json' was not found.")
            )
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {str(e)}"))
