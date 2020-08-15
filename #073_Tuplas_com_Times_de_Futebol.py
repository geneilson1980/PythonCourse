#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol na ordem de colocação. Depois mostre:
# A) Os 5 primeiros,
# B) Os últimos 4 colocados;
# C)Times em ordem alfabética;
# D) Em que posição está o time da Chapecoense.

classificacao = ("Porto", "Benfica", "Sporting", "Braga", "Famalicao", "Rio Ave", "Vitoria SC", "Santa Clara", "Moreirense", "Boavista", "Gil Vicente", "Pacos Ferreira", "Vitoria Setubal", "Belenenses", "Tondela", "Maritimo", "Portimonense", "Aves")
cont = len(classificacao)

print('-=' * 40)
print(f'Lista de times do campeonato Português: {classificacao}')
print('-=' * 40)
print('Os 5 primeiros colocados: ', end='')
print(classificacao[0:5])
print('-=' * 40)
print('Os 4 últimos colocados: ', end='')
print(classificacao[-4:])
print('-=' * 40)
print('Todos os times em ordem alfabética: ', end='')
print(f'{sorted(classificacao)}')
print('-=' * 40)
print(f'O Belenenses está na {classificacao.index("Belenenses")+1} posição')