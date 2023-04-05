import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        try:
            if path.endswith('.csv') != 1:
                raise ValueError("Arquivo inválido")
            csvfile = open(path, 'r')
            reader = csv.DictReader(csvfile)
            array = list()
            for info in reader:
                array.append(info)
            return array
        except ValueError:
            raise ValueError("Arquivo inválido")
