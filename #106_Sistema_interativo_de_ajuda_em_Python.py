# Faça um mini-sistema que utilize a interactividade help do python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra "FIM", o programa se encerrará.
# OBS: use cores.

def ajuda(com):
    print('\033[0;47m')
    help(com)
    # print('\033[0;47m')

def titulo(num):
    if num == 1:
        print('\033[0;42m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m')
        print('\033[0;42m   SISTEMA DE AJUDA PyHELP    \033[m')
        print('\033[0;42m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m')
    elif num == 2:
        print('\033[0;44m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m')
        print(f'\033[0;44m    Acessando o manual do comando "{obterAjuda}"     \033[m')
        print('\033[0;44m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m')
    else:
        print('\033[0;45m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m')
        print('\033[0;45m          ATÉ LOGO!           \033[m')
        print('\033[0;45m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m')



while True:
    titulo(1)
    obterAjuda = str(input('Digite a Função ou Biblioteca para ver a ajuda > '))
    if obterAjuda in 'fimFIM':
        titulo(3)
        break
    titulo(2)
    ajuda(obterAjuda)

    