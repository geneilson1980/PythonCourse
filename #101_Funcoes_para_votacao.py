# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def voto(ano):
    import datetime
    idade = datetime.datetime.now().year - ano
    if idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO!')
    elif idade < 18:
        print(f'Com {idade} anos: VOTO OPCIONAL!')
    elif idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')
    else:
        print(f'Com {idade} anos: VOTO OPCIONAL!')

print('-' * 30)
nascimento = int(input('Em que ano você nasceu? '))
voto(nascimento)