# Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os em 1 lista única que mantenha separados os valores pares e ímprares. No final, mostre os valores pares e ímpares em ordem crescente.

listaNmeros = [[], []]
i = 1
for i in range(1, 8):
    valor = int(input(f'Digite o {i}º valor: '))
    if valor % 2 == 0:
        listaNmeros[0].append(valor)
    else:
        listaNmeros[1].append(valor)
print('-=' * 40)
print(f'Os valores pares digitados foram: {sorted(listaNmeros[0])}')
print(f'Os valores impares digitados foram: {sorted(listaNmeros[1])}')