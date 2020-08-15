#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

# Ex.: Digite um número: 6.127 
#      O número 6.127 tem a parte inteira 6

#dica veja módulo math

import math

numeroDigitado = float(input("Digite um número real qualquer: "))
integerPart = math.modf(numeroDigitado)
integerPart2 = int(numeroDigitado)

print("O número digitado foi {} e a sua porção inteira é {:.0f}!".format(numeroDigitado, integerPart[1]))

print("O número digitado foi {} e a sua porção inteira é {}!".format(numeroDigitado, integerPart2))