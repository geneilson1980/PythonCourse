# faça um programa que tenha uma função chamada ficha() que receba 2 parâmetros opcionais:
#   O NOME de um jogador e quantos GOLS ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='<desconhecido>', gols=0):
    if nome != '' and gols != '':
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato')
    elif nome == '' and gols != '':
        print(f'O jogador <desconhecido> fez {gols} gol(s) no campeonato')
    elif nome != '' and gols == '':
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato')
    elif nome == '' and gols == '':
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

nomeJogador = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
golsJogador = ficha(nomeJogador, gols)
# golsJogador = ficha(nomeJogador, '')
# golsJogador = ficha('', gols)
