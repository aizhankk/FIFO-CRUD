from umag.models import Supply
import csv


def run():
    with open('umag/umaghacknu_supply.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Supply.objects.all().delete()

        for row in reader:
            print(row)

            # supply, _ = Supply.objects.get_or_create(name=row[-1])

            supply = Supply(id=row[0],
                        barcode=row[1],
                        quantity=row[2],
                        price=row[3],
                        supply_time=supply)
            supply.save()