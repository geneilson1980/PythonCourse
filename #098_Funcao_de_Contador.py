# Faça um programa que tenha uma função chamada contador() que receba 3 parametros: inicio, fim e passo. Seu programa tem que realizar 3 contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada.
import time

def Contador(inicio, fim, passo):
    if passo < 0:
        passo = abs(passo) 
    elif passo == 0:
        passo = 1
    if inicio < fim:
        print('-=' * 30)
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        while inicio <= fim:
            print(f'{inicio} ', end='')
            time.sleep(0.2)
            inicio += passo
        print('FIM!')
        print('-=' * 30)
    else:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        while inicio >= fim:
            print(f'{inicio} ', end='')
            time.sleep(0.2)
            inicio -= passo
        print('FIM!')
        print('-=' * 30)

Contador(1, 10, 1)
Contador(12, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
Contador(inicio, fim, passo)