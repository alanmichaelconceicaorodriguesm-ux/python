# python
Comandos de python.

produtos =["Teclado", "Mouse", "Monitor", "Impressora"]
busca = str(input("Digite o nome do produto que desejar buscar: "))

for i in produtos:
    if i == busca:
        print("Produto encontrado: ", i)
        break  

else:
    print("Produto não encontrado!")
