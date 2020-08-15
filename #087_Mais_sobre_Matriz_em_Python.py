# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores PARES digitados
# B) A soma dos valores da TERCEIRA coluna
# C) O MAIOR valor da segunda linha.

matriz = [[], [], []]
somaPares = 0
somaTColuna = 0
maiorValorSLinha = 0
for i in range(3):
    for j in range(3):
        valor = int(input(f'Digite uma valor para [{i}, {j}]: '))
        if valor % 2 == 0:
            somaPares += valor
        if j == 2:
            somaTColuna += valor
        if ((i == 1) and (valor > maiorValorSLinha)):
            maiorValorSLinha = valor
        matriz[i].append(valor)
print('-=' * 40)
for i in range(3):
    for j in range(3):
        print(f'[ {matriz[i][j]:^5} ]', end=' ')
    print()
print('-=' * 40)
print(f'A soma dos valores pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é {somaTColuna}')
print(f'O maior valor da segunda linha é {maiorValorSLinha}')