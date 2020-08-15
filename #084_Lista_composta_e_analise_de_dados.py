# Faça um programa que leia nome e peso de várias pessoas guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves

grupo = []
pessoa = []
maisPesados = []
maisLeves = []
contPessoa = 0
maiorPeso = 0
menorPeso = 0

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    pessoa.append(nome)
    contPessoa += 1
    pessoa.append(peso)
    # ATENCÃO, SEMPRE CRIAR CÓPIA DE DADOS PARA TRABALHAR INDEPENDENTE
    grupo.append(pessoa[:])
    pessoa.clear()
    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in 'nN':
        break
    if contPessoa == 1:
        # maiorPeso = peso
        menorPeso = peso
for p in grupo:
    if p[1] >= maiorPeso:
        if p[1] == maiorPeso:
            maiorPeso = p[1]
            maisPesados.append(p[0])
        else:
            maisPesados.clear()
            maiorPeso = p[1]
            maisPesados.append(p[0])
    elif p[1] <= menorPeso:
        if p[1] == menorPeso:
            menorPeso = p[1]
            maisLeves.append(p[0])
        else:
            maisLeves.clear()
            menorPeso = p[1]
            maisLeves.append(p[0])


print('-=' * 40)
print(f'Ao todo, você cadastrou {contPessoa} pessoas.')
print(f'O maior peso foi de {maiorPeso}Kg. Peso de {maisPesados}')
print(f'O menor peso foi de {menorPeso}Kg. Peso de {maisLeves}')