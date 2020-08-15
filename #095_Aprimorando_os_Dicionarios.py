# Aprimore o desafio #93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador.

# Tenho uma lista, dentro da lista, tenho um dicionário e dentro dos dicionarios eu tenho listas.


golsList = []
fichaTime = []
totalGols = 0
i = 0
estatisticaJogador = {}
golsJogador = []

while True:
    codigoJogador = i
    estatisticaJogador['cod'] = codigoJogador
    nomeJogador = str(input('Nome do jogador: '))
    estatisticaJogador['nome'] = nomeJogador
    partidas = int(input(f'Quantas partidas {nomeJogador} jogou? '))
    estatisticaJogador['partidas'] = partidas
    for x in range(0, partidas):
        gols = int(input(f'Quantos gols na partida {x}? '))
        golsJogador.append(gols)
        totalGols += gols
    estatisticaJogador['gols'] = golsJogador[:]
    estatisticaJogador['totalGols'] = totalGols
    fichaTime.append(estatisticaJogador.copy())
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar not in 'sSnN':
        while continuar not in 'sSnN':
            print('ERROR! Responda apenas S ou N.')
            continuar = str(input('Quer continuar? [S/N] '))
    elif continuar in 'nN':
        break
    totalGols = 0
    golsJogador = []
    estatisticaJogador = {}
    i += 1
print('-=' * 40)
for i in estatisticaJogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 80)
for k, v in enumerate(fichaTime):
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 80)
while True:
    mostrar = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if mostrar == 999:
        break
    if mostrar >= len(fichaTime):
        print(f'ERRO! Não existe jogador com código {mostrar}!')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {fichaTime[mostrar]["nome"]}:')
        for i, g in enumerate(fichaTime[mostrar]["gols"]):
            print(f'No jogo {i} fez {g} gols.')        
    print('-' * 80)
