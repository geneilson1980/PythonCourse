# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor = int(input('Digite um valor em metros: '))
centimetros = valor * 100
milimetros = valor * 1000

print('O valor em metros digitado foi {}, o seu valor correspondente em centímetros é {} e o seu valor em correspondente em milímetros é {}'.format(valor, centimetros, milimetros))