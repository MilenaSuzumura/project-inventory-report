from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(self):
        topInfo = SimpleReport.generate(self)
        arrayNome = []
        estoque = ''

        for product in self:
            arrayNome.append(product['nome_da_empresa'])

        nomeEmpresa = Counter(arrayNome).most_common()
        for empresa in nomeEmpresa:
            estoque += f"- {empresa[0]}: {empresa[1]}\n"

        return (
            f"{topInfo}\n"
            f"Produtos estocados por empresa:\n"
            f"{estoque}"
        )
