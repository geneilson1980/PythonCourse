# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a MÉDIA entre todos os valores e qual foi o MAIOR e o MENOR valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

numero = 0
cont = 0
media = 0
maior = 0
menor = 0
continuar = 's'
soma = 0
while continuar == 's':
    numero = int(input('Digite um número: '))
    if continuar == 's':
        cont += 1
        soma += numero        
        if numero > maior:
            maior = numero
        elif menor < numero:
            menor = numero
    continuar = str(input('Deseja continuar? [S/N] '))
media = soma / cont
print(f'Você digitou {cont} números e a média foi de {media:.2f}')
print(f'O maior valor foi de {maior} e o menor valor foi {menor}')