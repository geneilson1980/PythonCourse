# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma(). A primeira função vai sortear 5 números e vair colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
import time
import random

def sorteia():
    print(f'Sorteando 5 valores da lista:', end=' ')
    for i in range(5):
        numeros.append(random.randint(0, 20))
        print(f'{numeros[i]}', end=' ')
        time.sleep(0.2)
    print('PRONTO!')

def soma(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores PARES de {lista}, temos {soma}')

numeros = []
sorteia()
soma(numeros)
