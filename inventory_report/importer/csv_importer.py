import csv
from inventory_report.importer.importer import importer


class CsvImporter(importer):
    @classmethod
    def import_data(cls, path):
        try:
            csvfile = open(path, 'r')
            reader = csv.DictReader(csvfile)
            array = list()
            for info in reader:
                array.append(info)
            return array
        except ValueError:
            raise ValueError
