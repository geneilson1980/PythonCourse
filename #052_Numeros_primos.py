#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

numero = int(input('Digite um número inteiro: '))
numeroPrimo = True

for x in range(2, numero):
    if numero % x == 0:
        numeroPrimo = False
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(f'{x}', end='')

if numeroPrimo:
    print(f'\nO número {numero} é primo!')
else:
    print(f'\nO número {numero} não é primo porque ele é divisível por mais de um número!')

