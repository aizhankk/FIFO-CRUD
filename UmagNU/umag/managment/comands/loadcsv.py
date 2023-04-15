# # import csv
# # import re

# # from django.core.management.base import BaseCommand
# # from umag.models import Supply, Sale


# # class Command(BaseCommand):
# #     help = 'Loads data from a CSV file into the database'

# #     def add_arguments(self, parser):
# #         parser.add_argument('--csv', type=str, help='The path to the CSV file to load')

# #     def handle(self, *args, **options):
# #         csv_file_path = options['csv']
# #         with open(csv_file_path, 'r') as csv_file:
# #             reader = csv.DictReader(csv_file)
# #             for row in reader:
# #                 my_model = MyModel(id=row[0], barcode=row[1], quantity=row[2],price=row[3],sale_time=row[4])
# #                 my_model.save()


# import csv
# from django.core.management.base import BaseCommand
# from myapp.models import Supply

# class Command(BaseCommand):
#     help = 'Load data from a CSV file into the Supply model'

#     def add_arguments(self, parser):
#         parser.add_argument('csv_file', help='Path to the CSV file to load')

#     def handle(self, *args, **options):
#         csv_file_path = options['csv_file']
#         with open(csv_file_path) as csv_file:
#             reader = csv.DictReader(csv_file)
#             supplies = []
#             for row in reader:
#                 supply = Supply(
#                     barcode=row[0],
#                     quantity=row[1],
#                     price=row[2],
#                     supply_time=row[3]
#                 )
#                 supplies.append(supply)
#             Supply.objects.bulk_create(supplies)
#             self.stdout.write(self.style.SUCCESS('Successfully loaded CSV file into the Supply model'))
