# Desenvolva um programa que leia o primerio termo e a razão de uma PA, no final, mostre os 10 primeiros termos dessa progressão.

# razao = pega um termo e subrtrai pelo anterior

primeiroTermo = int(input('Digite o primeito termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termos = primeiroTermo

for x in range(1, 11):
    print(f'O {x}º termo da PA é: {termos}')
    termos+= razao