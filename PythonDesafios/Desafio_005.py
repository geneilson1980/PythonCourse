# Faça um programa que leia um número inteiro e mostra na tela o seu sucessor e seu antecessor
numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1

print('O número digitado foi {}, o seu antecessor é {} e o seu sucessor é {}'.format(numero, antecessor, sucessor))