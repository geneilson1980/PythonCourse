# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

precoProduto = float(input("Digite o preço do produto: "))
desconto = 5
precoDesconto = precoProduto - ((precoProduto / 100) * desconto)

print("O valor original do produto era de R$ {:.2f} reais, aplicando o desconto de {}%, você irá pagar somente R$ {:.2f} reais!".format(precoProduto, desconto, precoDesconto))