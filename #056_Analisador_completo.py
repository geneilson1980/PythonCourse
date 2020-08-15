# Desenvolva um programa que leia: O nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo
# Qual o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos.

pessoas = {}
somaIdade = 0
mediaIdade = 0
homemMaisVelho = 0
nomeHMaisVelho = ''
countMulheres = 0

for x in range(1, 5):
    print(f'----- {x}ª PESSOA -----')
    pessoas[f'pessoa{x}'] = {'nome': str(input('Nome: ')), 'idade': int(input('Idade: ')), 'sexo': str(input('Sexo[M/F]: '))}
    if pessoas[f'pessoa{x}']['idade'] > homemMaisVelho and pessoas[f'pessoa{x}']['sexo'] == 'm':
        homemMaisVelho = pessoas[f'pessoa{x}']['idade']
        nomeHMaisVelho = pessoas[f'pessoa{x}']['nome']
    if pessoas[f'pessoa{x}']['sexo'] == 'f' and pessoas[f'pessoa{x}']['idade'] < 20:
        countMulheres += 1

    somaIdade += pessoas[f'pessoa{x}']['idade']

sizeDic = len(pessoas)
mediaIdade = somaIdade / sizeDic

print(f'\na média de idade do grupo é: {mediaIdade} anos')
print(f'O nome do homem mais velho do grupo é: {nomeHMaisVelho}')
print(f'Existem {countMulheres} mulhere(s) com menos de 20 anos no grupo')