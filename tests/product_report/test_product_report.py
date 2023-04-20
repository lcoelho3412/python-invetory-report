from inventory_report.inventory.product import Product


def test_create_product():
    product = Product(
        id=95432,
        nome_do_produto="Produto ficticio",
        nome_da_empresa="Empresa ficticia",
        data_de_fabricacao="10/08/2019",
        data_de_validade="25/08/2024",
        numero_de_serie="nsf021585",
        instrucoes_de_armazenamento="local seco e arejado"
    )

    assert product.id == 95432
    assert product.nome_do_produto == "Produto ficticio"
    assert product.nome_da_empresa == "Empresa ficticia"
    assert product.data_de_fabricacao == "10/08/2019"
    assert product.data_de_validade == "25/08/2024"
    assert product.numero_de_serie == "nsf021585"
    assert product.instrucoes_de_armazenamento == "local seco e arejado"
