# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
i = 0
while i < 5:
    valor = int(input(f'Digite o {i+1}º valor para a posição {i}: '))
    lista.append(valor) 
    i+=1
menor = lista[0]
maior = lista[0]
print('=-' * 40)
print(f'Você digitou os valores {lista}')
for valor in lista:
    if valor < menor:
        menor = valor
    if valor > maior:
        maior = valor
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
i = 0
while i < len(lista):
    if lista[i] == maior:
        print(f'{i:.<4}', end=' ')
    i+=1
print(f'\nO menor valor digitado foi {menor} nas posições', end=' ')
j = 0
while j < len(lista):
    if lista[j] == menor:
        print(f'{j:.<4}', end=' ')
    j+=1