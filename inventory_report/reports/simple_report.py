from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(self):
        timeNow = datetime.now().strftime("%Y-%m-%d")
        fabricacaoMaisAntiga = timeNow
        arrayValidade = []
        arrayNome = []

        for product in self:
            if fabricacaoMaisAntiga > product['data_de_fabricacao']:
                fabricacaoMaisAntiga = product['data_de_fabricacao']

            if timeNow < product['data_de_validade']:
                arrayValidade.append(product['data_de_validade'])
            arrayNome.append(product['nome_da_empresa'])

        """ info: https://docs.python.org/3/library/collections.html """
        nomeEmpresa = Counter(arrayNome).most_common(1)

        return (
            f"Data de fabricação mais antiga: {fabricacaoMaisAntiga}\n"
            f"Data de validade mais próxima: {min(arrayValidade)}\n"
            f"Empresa com mais produtos: {nomeEmpresa[0][0]}"
        )
