produtos = ["Teclado", "Mouse", "Monitor", "Impressora"]
# Cria uma lista com os produtos disponíveis.

busca = input("Digite o nome do produto que desejar buscar: ")
# Solicita a entrada do usuário.
# O valor digitado já é armazenado como texto.

for i in produtos:
# Percorre cada item da lista.
# A variável i recebe um produto por vez.

    if i == busca:
    # Compara o produto atual com o valor informado.

        print("Produto encontrado:", i)
        # Exibe o produto encontrado.

        break
        # Interrompe o loop após encontrar o produto.

else:
# Executa somente se o loop não foi interrompido pelo break.

    print("Produto não encontrado!")
    # Informa que nenhum produto correspondeu à busca.
