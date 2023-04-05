from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, relatorio):
        if path.endswith('.csv') == 1:
            isPath = CsvImporter.import_data(path)
            return RelatorioTerminado.import_data(isPath, relatorio)

        if path.endswith('.json') == 1:
            isPath = JsonImporter.import_data(path)
            return RelatorioTerminado.import_data(isPath, relatorio)

        if path.endswith('.xml') == 1:
            isPath = XmlImporter.import_data(path)
            return RelatorioTerminado.import_data(isPath, relatorio)


class RelatorioTerminado:
    @staticmethod
    def import_data(path, relatorio):
        if relatorio == 'simples':
            simple = SimpleReport.generate(path)
            return simple

        if relatorio == 'completo':
            complet = CompleteReport.generate(path)
            return complet
