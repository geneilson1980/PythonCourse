# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra
# B) Quantos produtos custam mais de R$1000
# C) Qual é nome do produto mais barato.

totalGasto = 0
prdMaior1000 = 0
prdMaisBarato = 0
nomePrdMaisBarato = ''
contPrd = 0
    
print('-' * 40)
print('LOJA SUPER BARATÃO')
print('-' * 40)
while True:
    nomeProduto = str(input('Nome do produto: '))
    precoProduto = float(input('Preço: R$ '))
    totalGasto += precoProduto
    contPrd += 1
    if contPrd == 1:
        prdMaisBarato = precoProduto
        nomePrdMaisBarato = nomeProduto
    if precoProduto > 1000:
        prdMaior1000 += 1
    if precoProduto < prdMaisBarato:
        prdMaisBarato = precoProduto
        nomePrdMaisBarato = nomeProduto
    continuar = str(input('Quer continuar? [S/N]')).upper()
    if continuar != 'S':
        print('-' * 15, end='' )
        print('FIM DO PROGRAMA', end='')
        print('-' * 15)
        break
print(f'O total da compra foi R${totalGasto:.2f}')
print(f'Temos {prdMaior1000} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi a/o {nomePrdMaisBarato} que custa R${prdMaisBarato:.2f}')


