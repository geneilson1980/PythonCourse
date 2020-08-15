# Faça um programa que leia um número qualquer e mostre o seu fatorial

# Ex.:
# 5! = 5x4x3x2x1 = 120

numero = int(input('Digite um número para calcular o seu fatorial: '))
fatorial = 1

print(f'Calculando {numero}! = {numero} x ', end='')
while numero > 1:
    fatorial = fatorial * numero
    numero -=1
    if numero == 1:
        print(f'{numero} = ', end='')
    else:
        print(f'{numero} x ', end='')

print (fatorial)