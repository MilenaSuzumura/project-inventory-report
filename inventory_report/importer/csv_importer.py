import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
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
            raise 'Arquivo inválido'
