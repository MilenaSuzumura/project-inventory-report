import csv
import json
from xml.etree.ElementTree import ElementTree
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, relatorio):
        if path.endswith('.csv') == 1:
            return CsvImporter.import_data(path, relatorio)

        if path.endswith('.json') == 1:
            return JsonImporter.import_data(path, relatorio)

        if path.endswith('.xml') == 1:
            return XmlImporter.import_data(path, relatorio)


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
        if relatorio == 'simples':
            jsonFile = open(path, 'r')
            reader = json.load(jsonFile)
            simple = SimpleReport.generate(reader)
            return simple

        if relatorio == 'completo':
            jsonFile = open(path, 'r')
            reader = json.load(jsonFile)
            complet = CompleteReport.generate(reader)
            return complet


class XmlImporter:
    @staticmethod
    def import_data(path, relatorio):
        if relatorio == 'simples':
            xmlFile = open(path, 'r')
            tree = ElementTree()
            reader = tree.parse(xmlFile)
            array = list()
            for info in reader:
                id = info.find("id").text
                nome_do_produto = info.find("nome_do_produto").text
                nome_da_empresa = info.find("nome_da_empresa").text
                data_de_fabricacao = info.find("data_de_fabricacao").text
                data_de_validade = info.find("data_de_validade").text
                numero_de_serie = info.find("numero_de_serie").text
                instrucoes_de_armazenamento = info.find(
                    "instrucoes_de_armazenamento"
                ).text
                array.append({
                    "id": id,
                    "nome_do_produto": nome_do_produto,
                    "nome_da_empresa": nome_da_empresa,
                    "data_de_fabricacao": data_de_fabricacao,
                    "data_de_validade": data_de_validade,
                    "numero_de_serie": numero_de_serie,
                    "instrucoes_de_armazenamento": instrucoes_de_armazenamento,
                })
            simple = SimpleReport.generate(array)
            return simple

        if relatorio == 'completo':
            xmlFile = open(path, 'r')
            tree = ElementTree()
            reader = tree.parse(xmlFile)
            array = list()
            for info in reader:
                id = info.find("id").text
                nome_do_produto = info.find("nome_do_produto").text
                nome_da_empresa = info.find("nome_da_empresa").text
                data_de_fabricacao = info.find("data_de_fabricacao").text
                data_de_validade = info.find("data_de_validade").text
                numero_de_serie = info.find("numero_de_serie").text
                instrucoes_de_armazenamento = info.find(
                    "instrucoes_de_armazenamento"
                ).text
                array.append({
                    "id": id,
                    "nome_do_produto": nome_do_produto,
                    "nome_da_empresa": nome_da_empresa,
                    "data_de_fabricacao": data_de_fabricacao,
                    "data_de_validade": data_de_validade,
                    "numero_de_serie": numero_de_serie,
                    "instrucoes_de_armazenamento": instrucoes_de_armazenamento,
                })
            complet = CompleteReport.generate(array)
            return complet
