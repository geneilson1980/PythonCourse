# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
import locale

def aumentar(num, formato=False):
    '''
    teste
    '''

    result = num + ((num / 100) * 10)
    # currency = moeda(result)
    if formato is False:
        return result
    else:
        return moeda(result)

def diminuir(num, per=0, formato=False):
    result = num - ((num / 100) * per)
    # currency = moeda(result)
    if formato is False:
        return result
    else:
        return moeda(result)    

def metade(num, formato=False):
    result = num / 2
    # currency = moeda(result)
    if formato is False:
        return result
    else:
        return moeda(result)

def dobro(num, formato=False):
    result = num * 2
    # currency = moeda(result)
    if formato is False:
        return result
    else:
        return moeda(result)

def resumo(num, formato=False):
    print('-' * 30)
    print('       RESUMO DO VALOR')
    print('-' * 30)
    print(f'{"Preço analisado: ":<20}', end='')
    print(moeda(num))
    print(f'{"Dobro do preço: ":<20}', end='')
    print(dobro(num, True))
    print(f'{"Metade do preço: ":<20}', end='')
    print(metade(num, True))
    print(f'{"80% de aumento: ":<20}', end='')
    print(diminuir(num, 80, True))
    print(f'{"35% de redução: ":<20}', end='')
    print(diminuir(num, 35, True))
    print('-' * 30)

def moeda(value):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    currency = locale.currency(value, grouping=True, symbol=True)
    return currency