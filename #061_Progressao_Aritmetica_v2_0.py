# Faça o desafio 051 lendo o primeiro termo e a razão de uma PA mostrando os 10 primeiros termos da progressão usando a estrutura while

print('Gerador de PA')
print('-='*20)

primeiroTermo = int(input('Digite o primeito termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termos = primeiroTermo
count = 0

while count < 10:
    print(f'{termos} -> ', end='')
    termos+= razao
    count+=1
print('FIM')