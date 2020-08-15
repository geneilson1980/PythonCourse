# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10 só que agora o jogador vai tentar adivinhar até acertar mostrando no final quantos palpites foram necessários para vencer.

import random
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

numeroComputador = random.randrange(0, 10)
palpiteJogador = int(input('Qual o seu palpite? '))
count = 0

while palpiteJogador != numeroComputador:
    if palpiteJogador < numeroComputador:
        print('Mais... Tente mais uma vez.')
        palpiteJogador = int(input('Qual o seu palpite? '))
        count+=1
    else:
        print('Menos... Tente mais uma vez.')
        palpiteJogador = int(input('Qual o seu palpite? '))
        count+=1

if count == 0:
    print(f'PARABÉNS! Acertou de primeira. O número que eu pensei foi exatamente {palpiteJogador}')
else:
    print(f'PARABÉNS! Acertou depois de {count+1} tentativas. O número que eu pensei foi {palpiteJogador}')