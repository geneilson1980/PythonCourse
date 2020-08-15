# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas cadastradas
# B) A média de idade
# C) Uma lista com mulheres
# D) Uma lista com idade acima da média.

listaPessoas = []
i = 1

while True:
    locals()[f'dadosPessoas{i}'] = {}
    nome = str(input('Nome: '))
    locals()[f'dadosPessoas{i}']['nome'] = nome
    sexo = str(input('Sexo: [M/F] '))
    if sexo not in 'mMfF':
        while sexo not in 'mMfF':
            print('ERRO! Por favor, digite apenas M ou F!')
            sexo = str(input('Sexo: [M/F] '))
        locals()[f'dadosPessoas{i}']['sexo'] = sexo
    else:
        locals()[f'dadosPessoas{i}']['sexo'] = sexo
    idade = int(input('Idade: '))
    listaPessoas.append(locals()[f'dadosPessoas{i}'])
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar not in 'sSnN':
        while continuar not in 'sSnN':
            print('ERROR! Responda apenas S ou N.')
            continuar = str(input('Quer continuar? [S/N] '))
    elif continuar in 'nN':
        break
    i += 1
countPessoas = len(listaPessoas)
print(f'Foram cadastradas {countPessoas} pessoas')
