# Crie um programa que vai gerar cinco númeors aleatórios e colocar em uma tupla. depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random

aTuple = ()
for i in range(5):
    aTuple = aTuple + (random.randint(1, 10),)

aTupleSize = len(aTuple)
menorValor = aTuple[0]
# menorValor = min(aTuple)
# maiorValor = max(aTuple)
maiorValor = 0
print(f'Os valores sorteados foram: ', end='')
for i in range(aTupleSize):
    if aTuple[i] > maiorValor:
        maiorValor = aTuple[i]
    if aTuple[i] < menorValor:
        menorValor = aTuple[i]
    print(f'{aTuple[i]} ', end='')

print(f'\nO maior valor sorteado foi {maiorValor}')
print(f'O menor valor sorteado foi {menorValor}')