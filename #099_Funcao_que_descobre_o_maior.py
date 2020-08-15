# Faça uma programa que tenha uma função chamada maior() que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles e o maior.

# Packages parameters.
import time
def maior(* num):
    print('-=' * 40)
    print('Analisando os valores passados...')
    time.sleep(0.2)
    for valor in num:
        print(f'{valor}', end=' ')
        time.sleep(0.2)
    print(f'Foram informados {len(num)} valores ao todo.')
    maior = num[0]
    for i in num:
        if i > maior:
            maior = i
    print(f'O maior valor informado foi {maior}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
