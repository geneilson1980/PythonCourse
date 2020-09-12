# import math
# from math import sqrt

# Escreva um programa que leia um número real qualqer pelo teclado e mostre nat ela a sua porção inteira
# Ex: Digite um número: 6.127
#     O número 6.127 tem a parte inteira 6.

# import math
from math import trunc
numeroReal = float(input('Digite um número real qualquer: '))
# parteInteira = math.trunc(numeroReal)
parteInteira = trunc(numeroReal)

print(f'O número {numeroReal} tem a parte inteira {parteInteira}')