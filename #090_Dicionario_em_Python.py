# Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

boletimAluno= {}

aluno = str(input('Nome: '))
boletimAluno['nome'] = aluno
media = float(input(f'Média de {aluno}: '))
boletimAluno['media'] = media
if media < 5:
    situacao = 'Reprovado'
elif media < 7:
    situacao = 'Recuperação'
else:
    situacao = 'Aprovado'
boletimAluno['situacao'] = situacao

print('-=' * 40)
# print(f'- Nome é igual a {aluno}')
# print(f'- Média é igual a {media}')
# print(f'- A situação do aluno é {situacao}')

for k, v in boletimAluno.items():
    print(f'{k} é igual a {v}')
