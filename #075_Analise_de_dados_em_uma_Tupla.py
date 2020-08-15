# Desenvolva um programa que leia 4 valores pelo teclado e guarde em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9
# B) em que posição foi digitado o valor 3.
# C) Quais foram os números pares.

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
numero_3 = int(input('Digite mais um número: '))
numero_4 = int(input('Digite o último número: '))
numeros = (numero_1, numero_2, numero_3, numero_4)
pares = []
cont9 = 0

for i in range(4):
    if numeros[i] == 9:
        cont9+=1
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])

print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {cont9} vezes')
print(f'O valor 3 apareceu na posição {numeros.index(3)+1}')
print('Os valores pares digitados foram: ', end='')
for i in range(len(pares)):
    if i != len(pares)-1:
        print(f'{pares[i]},', end=' ')
    else:
        print(f'{pares[i]}')
