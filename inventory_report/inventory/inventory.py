import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
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
