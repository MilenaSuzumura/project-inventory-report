from inventory_report.inventory.product import Product

id = 1
nome_do_produto = 'Lápis de cor'
nome_da_empresa = 'Faber'
data_de_fabricacao = '2022'
data_de_validade = '2023'
numero_de_serie = 'ASADJAD24'
instrucoes_de_armazenamento = 'Mantenha em local seco'


def test_cria_produto():
    infoProduct = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert infoProduct.id == id
    assert infoProduct.nome_do_produto == nome_do_produto
    assert infoProduct.nome_da_empresa == nome_da_empresa
    assert infoProduct.data_de_fabricacao == data_de_fabricacao
    assert infoProduct.data_de_validade == data_de_validade
    assert infoProduct.numero_de_serie == numero_de_serie
    assert (
        infoProduct.instrucoes_de_armazenamento == instrucoes_de_armazenamento
    )
