# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

print('-'*20)
print('Sequência de Fibonacci')
print('-'*20)

termos = int(input('Quantos termos você quer mostrar? '))
fibonacci = 0
print('~'*20)
countTermos = 1

while countTermos <= termos:
    if countTermos == 1:
        fibonacci = 0
        print(f'{fibonacci} -> ', end='')
        countTermos += 1
        valorA = fibonacci
    elif countTermos == 2 or countTermos == 3:
        fibonacci = 1
        print(f'{fibonacci} -> ', end='')
        countTermos += 1
        valorA = fibonacci
        valorB = fibonacci
    else:
        fibonacci = valorA + valorB
        print(f'{fibonacci} -> ', end='')
        countTermos += 1
        valorA = valorB
        valorB = fibonacci
print('FIM')
print('~'*20)

def fibo(n):
    print()