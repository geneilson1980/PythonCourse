# Melhore o DESAFIO 061 perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')
print('-='*20)

primeiroTermo = int(input('Digite o primeito termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termos = primeiroTermo
count = 0
qtdTermos = 0

while count < 10:
    print(f'{termos} -> ', end='')
    termos+= razao
    count+=1
    qtdTermos+=1
print('PAUSA')

termosAMais = int(input('Quantos termos quer mostrar a mais? '))
countMais = 0
while termosAMais != 0:
    while countMais < termosAMais:
        if termosAMais == 0:
            break
        print(f'{termos} -> ', end='')
        termos+= razao
        countMais+=1
        qtdTermos+=1
    print('PAUSA')
    termosAMais = int(input('Quantos termos quer mostrar a mais? '))
    countMais = 0
print(f'Progressão finalizada com {qtdTermos} termos mostrados.')
