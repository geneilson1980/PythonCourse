# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos duratne o campeonato.

estatisticaJogador = {}
golsList = []
totalGols = 0
nomeJogador = str(input('Nome do jogador: '))
estatisticaJogador['nome'] = nomeJogador
partidas = int(input(f'Quantas partidas {nomeJogador} jogou? '))
# estatisticaJogador['partidas'] = partidas
for x in range(1, partidas+1):
    gols = int(input(f'Quantos gols na partida {x}? '))
    totalGols += gols
    golsList.append(gols)
estatisticaJogador['gols'] = golsList[:]
estatisticaJogador['total'] = totalGols
print('-=' * 40)
print(estatisticaJogador)
print('-=' * 40)
for k, v in estatisticaJogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 40)
print(f'O jogador {estatisticaJogador["nome"]} jogou {partidas} partidas.')
for x, y in enumerate(estatisticaJogador['gols']):
    print(f'    => Na partida {x+1}, fez {y} gols.')
print(f'Marcou um total de {estatisticaJogador["total"]} gols.')