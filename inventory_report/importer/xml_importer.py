from xml.etree import ElementTree
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        try:
            if path.endswith('.xml') != 1:
                raise ValueError("Arquivo inválido")
            xmlFile = open(path, 'r')
            tree = ElementTree.ElementTree()
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
            return array
        except ValueError:
            raise ValueError("Arquivo inválido")
