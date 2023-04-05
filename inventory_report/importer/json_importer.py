import json
from inventory_report.importer.importer import importer


class JsonImporter(importer):
    @classmethod
    def import_data(cls, path):
        try:
            jsonFile = open(path, 'r')
            reader = json.load(jsonFile)
            return reader
        except ValueError:
            raise ValueError
