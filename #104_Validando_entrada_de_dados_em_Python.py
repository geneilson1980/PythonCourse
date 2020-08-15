# Crie um programa que tenha a função leiaInt() que vai funcionar de forma semelhante à função input() do python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex:
#   n=leialnt('Digite um n')

def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            print(f'Você acabou de digitar o número {n}')
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            break

n = leiaInt('Digite um número: ')










# def leiaInt(msg):
#     # ok = False
#     # valor = 0
#     while True:
#         n = str(input(msg))
#         if n.isnumeric():
#             # valor = int(n)
#             # ok = True
#             print(f'Você acabou de digitar o número {n}')
#             break
#         else:
#             print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
#             break
#         # if ok:
#             # break
#     # return valor

# n = leiaInt('Digite um número: ')
# # print(f'Você acabou de digitar o número {n}')
