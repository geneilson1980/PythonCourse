# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
catetoOposto = float(input('Digite o valor do cateto oposto do triângulo: '))
catetoAdjacente = float(input('Digite o valor do cateto adjacente do triângulo: '))
hipotenusa = hypot(catetoOposto, catetoAdjacente)

print(f'O valor do Cateto oposto é {catetoOposto}, o valor do cateto adjacente é {catetoAdjacente} e o comprimento da hipotenusa é: {hipotenusa:.2f}')