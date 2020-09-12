# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

# Considere U$$ 1.00 = R$ 3,27

valor = float(input('Digite o valor em Reais que tem na carteira: '))
converte = float(valor / 3.27)

print('O valor em reais que tem na carteira é de R$ {:.2f}. Esse valor pode comprar U$$ {:.2f} Dólares atualmente'.format(valor, converte))