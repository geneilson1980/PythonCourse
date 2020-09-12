#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
print('Vou pensar em um número inteiro entre 0 e 5. Tente adivinhar...')
numero = random.randrange(5)
entradaUsuario = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')

if(entradaUsuario == numero):
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'PERDEU! Você não conseguiu acertar o número. O número que eu pensei foi {numero}!')
