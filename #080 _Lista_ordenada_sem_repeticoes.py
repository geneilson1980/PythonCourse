# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista já na posição corrta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

import bisect
orderedList = []

for x in range(5):
    valor = int(input('Digite um a valor: '))
    posicao = bisect.bisect(orderedList, valor)
    bisect.insort(orderedList, valor)
    if valor == max(orderedList):
        print(f'Adicionado ao final da lista...')
    else:
        print(f'Adicionado na posição {posicao} da lista...')

print('-=' * 40)
print(f'Os valores digitados em ordem foram {orderedList}')