# Faça um programa que jogue par ou ímpar com o computador. O jogo será interompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
print('=-' * 40)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 40)
cont = 0

while True:
    valorJogador = int(input('Digite um valor: '))
    parOuImparJogador = str(input('Par ou Impar? [P/I]' ))
    print('-' * 40)
    valorComputador = random.randint(1, 100)
    soma = valorJogador + valorComputador
    result = 'PAR'
    if soma % 2 == 0:
        parOuImparComputador = 'P'
    else:
        parOuImparComputador = 'I'
        result = 'ÍMPAR'
    print(f'Você jogou {valorJogador} e o computador {valorComputador}. Total de {soma}. Deu {result}')
    print('-' * 40)
    if parOuImparJogador == parOuImparComputador:
        print('Você VENCEU!')
        print('Vamos jogar mais uma vez')
        cont += 1
    else:
        print('Você PERDEU!')
        print('=-' * 40)
        break
print(f'GAME OVER! Você venceu {cont} vezes!')

    


