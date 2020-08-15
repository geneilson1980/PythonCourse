# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

import random, operator,time
jogoDados = {}
ranking = {}
jogada = 0
jogador = 'jogador'
print('Valores sorteados:')
for x in range(1, 5):
    time.sleep(1)
    jogador += str(x)
    jogada = random.randint(1, 6)
    jogoDados[jogador] = jogada
    print(f'{jogador} tirou {jogada} no dado.')
    jogador = 'jogador'
print('-=' * 40)
print('== RANKING DOS JOGADORES ==')
ranking = dict(sorted(jogoDados.items(), key=operator.itemgetter(1), reverse=True))
a = 1
for k,v in ranking.items():
    time.sleep(1)
    print(f'{a}° lugar: {k} com {v}')
    a += 1
