# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
#temos um círculo, o eixo vertical é o seno, o eixo horizontal é o cosseno (tem função no módullo pra isso)

import math

angulo = float(input('Digite o valor do ângulo desejado: '))
convert = math.radians(angulo)
seno = math.sin(convert)
cosseno = math.cos(convert)
tangente = math.tan(convert)

print(f'O seno de {angulo}º é {seno:.2f}, o cosseno é {cosseno:.2f} e a tangente é {tangente:.2f}')
