# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
numero = int(input('Digite um número inteiro: '))

print('A tabuada do número {} é:!'.format(numero))
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(numero + 1):
    multi = numero * x 
    print('{} x {} = {}'.format(numero, x, multi))