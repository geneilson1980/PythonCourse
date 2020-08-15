# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
# No final, mostre a matriz na tela com a formatação correta.

matriz = [[], [], []]

for i in range(3):
    for j in range(3):
        valor = int(input(f'Digite uma valor para [{i}, {j}]: '))
        matriz[i].append(valor)
print('-=' * 40)
for i in range(3):
    for j in range(3):
        print(f'[ {matriz[i][j]:^5} ]', end=' ')
    print()