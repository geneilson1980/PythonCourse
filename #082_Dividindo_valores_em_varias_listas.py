# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie 2 listas extras que vao conter apenas os valores pares e os valores ímpares digitados respectivamente. Ao final, mostre o conteúdo das 3 listas geradas.

listaGeral = []
listaPares = []
listaImpares = []

while True:
    valor = int(input('Digite um número: '))
    listaGeral.append(valor)
    if valor % 2 == 0:
        listaPares.append(valor)
    else:
        listaImpares.append(valor)

    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'nN':
        break
print('-=' * 40)
print(f'a lista completa é {listaGeral}')
print(f'a lista de pares é {listaPares}')
print(f'a lista de ímpares é {listaImpares}')