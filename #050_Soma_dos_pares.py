#Desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares, se o valor digitado for Impar, desconsidere-o

soma = 0
for x in range(1, 7):
    numero = int(input(f'Digite o {x}º valor: '))
    if numero % 2 == 0:
        soma+= numero
print(soma)