# Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os mostrando na tela uma mensagem:
# - O PRIMEIRO VALOR é MAIOR
# - o SEGUNDO VALOR é MAIOR
# - NÃO EXISTE valor maior, os dois são IGUAIS

primeiroValor = int(input('Digite o primeiro valor para ser comparado: '))
segundoValor = int(input('Digite o segundo valor para ser comparado: '))

if primeiroValor > segundoValor:
    print('O primeiro valor á maior')
elif segundoValor > primeiroValor:
    print('O segundo valor á maior')
else:
    print('Não existe valor maior, os dois são iguas')