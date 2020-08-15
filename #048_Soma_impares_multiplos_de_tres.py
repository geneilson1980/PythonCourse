#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500

#A soma de todos os 83 valores sollicitados é 20667

soma = 0
count = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        count += 1
        soma = soma + n    

print(f'A soma de todos os {count} valores sollicitados é {soma}')
