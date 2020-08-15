#Crie um programa que leia vários numeros inteiros pelo teclado. O programa só vai parar quando o usuáro digitar o valor 999 que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

numero = 0
soma = 0
cont = 0

while numero != 999:
    numero = int(input("Digite um número [999 para parar]: "))
    if numero != 999:
        soma+= numero
        cont+= 1

print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
