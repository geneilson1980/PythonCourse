# Crie um programa que tenha uma tupla única com nome de produtos e seus respectivos preços em sequência. No final, mostre uma listagem de preços organizando os dados em forma tabular.

import pandas as pd

print('-' * 40)
print('LISTAGEM DE PREÇOS'.center(40, " "))
print('-' * 40)
produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 4.90, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

for x in range(0, len(produtos)):
    if x % 2 == 0:
        print(f'{produtos[x]:.<30}', end=' ')
    else:
        print(f'R${produtos[x]:>7}')
print('-' * 40)