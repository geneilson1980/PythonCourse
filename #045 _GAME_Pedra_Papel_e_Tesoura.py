# Crie um programa que faça o computador jogar JOKENPÔ com você

import random, time

print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

jogadaJogador = int(input('Qual é a sua jogada? '))
jogadaComputador = random.randint(0,2)
print('JO')
time.sleep(0.2)
print('KEN')
time.sleep(0.2)
print('PÔ!!!')

print('-='*22)
if jogadaJogador == 0:
    if jogadaComputador == 0:        
        print(f'Computador jogou PEDRA')
        print(f'Jogador jogou PEDRA')
        print('-='*22)
        print('EMPATE')
    elif jogadaComputador == 1:
        print(f'Computador jogou PAPEL')
        print(f'Jogador jogou PEDRA')
        print('-='*22)
        print('COMPUTADOR VENCE')
    elif jogadaComputador == 2:
        print(f'Computador jogou TESOURA')
        print(f'Jogador jogou PEDRA')
        print('-='*22)
        print('JOGADOR VENCE')
elif jogadaJogador == 1:
    if jogadaComputador == 0:        
        print(f'Computador jogou PEDRA')
        print(f'Jogador jogou PAPEL')
        print('-='*22)
        print('JOGADOR VENCE')
    elif jogadaComputador == 1:
        print(f'Computador jogou PAPEL')
        print(f'Jogador jogou PAPEL')
        print('-='*22)
        print('EMPATE')
    elif jogadaComputador == 2:
        print(f'Computador jogou TESOURA')
        print(f'Jogador jogou PAPEL')
        print('-='*22)
        print('COMPUTADOR VENCE')
elif jogadaJogador == 2:
    if jogadaComputador == 0:        
        print(f'Computador jogou PEDRA')
        print(f'Jogador jogou TESOURA')
        print('-='*22)
        print('COMPUTADOR VENCE')
    elif jogadaComputador == 1:
        print(f'Computador jogou PAPEL')
        print(f'Jogador jogou TESOURA')
        print('-='*22)
        print('JOGADOR VENCE')
    elif jogadaComputador == 2:
        print(f'Computador jogou TESOURA')
        print(f'Jogador jogou TESOURA')
        print('-='*22)
        print('EMPATE')
