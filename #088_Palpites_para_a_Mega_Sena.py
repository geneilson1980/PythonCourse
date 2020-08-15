# Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo. cadastrando tudo em uma lista composta.

import random
import time
jogosTotal = []
jogo = []
print('-' * 40)
print('JOGA NA MEGA SENA'.center(40))
print('-' * 40)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {jogos} JOGOS-=-=-=')
for i in range(jogos):
    for j in range(6):
        numero = random.randint(1, 60)
        jogo.append(numero)
    jogosTotal.append(jogo[:])
    jogo.clear()

a = len(jogosTotal)
for i in range(len(jogosTotal)):
    print(f'Jogo {i+1}: ', end = ' ')
    print(jogosTotal[i])
    time.sleep(0.5)
print(f'-=-=-= < BOA SORTE! > -=-=-=')