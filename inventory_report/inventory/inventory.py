import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, relatorio):
        if path.endswith('.csv') == 1:
            return CsvImporter.import_data(path, relatorio)

        if path.endswith('.json') == 1:
            return False

        if path.endswith('.xml') == 1:
            return False


class CsvImporter:
    @staticmethod
    def import_data(path, relatorio):
        if relatorio == 'simples':
            csvfile = open(path, 'r')
            reader = csv.DictReader(csvfile)
            array = list()
            for info in reader:
                array.append(info)
            simple = SimpleReport.generate(array)
            return simple

        if relatorio == 'completo':
            csvfile = open(path, 'r')
            reader = csv.DictReader(csvfile)
            array = list()
            for info in reader:
                array.append(info)
            complet = CompleteReport.generate(array)
            return complet


class JsonImporter:
    @staticmethod
    def import_data(path, relatorio):
        return False


class XmlImporter:
    @staticmethod
    def import_data(path, relatorio):
        return False
