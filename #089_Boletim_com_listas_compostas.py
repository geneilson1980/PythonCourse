# Crie um programa que leia nome e 2 notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usu+ario possa mostrar as notas de cada aluno individualmente.
import tabulate
listaGeral = []
aluno = []
numero = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    aluno.append(numero)
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    aluno.append(media)
    listaGeral.append(aluno[:])
    aluno.clear() 
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'nN':
        print('-=' * 40)
        break
    numero += 1
print(f'{"Nº":<10}', end=' ')
print(f'{"NOME":<20}', end=' ')
print(f'{"MÉDIA":>8}')
print('-=' * 30)
for i in range(len(listaGeral)):
    # print(tabulate.tabulate({"Nº": [listaGeral[i][0]], "NOME": [listaGeral[i][1]], "MÉDIA": [listaGeral[i][4]]}, headers="keys"))
    print(f'{listaGeral[i][0]:<10}', end='')
    print(f'{listaGeral[i][1]:<20}', end='')
    print(f'{listaGeral[i][4]:>8.2f}', end='')
    print()
print('-=' * 30)
mostrarNotas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
while True:
    if mostrarNotas != 999:
        print(f'Notas de {listaGeral[mostrarNotas][1]} são: [{listaGeral[mostrarNotas][2]}, {listaGeral[mostrarNotas][3]}]')
        print('-=' * 30)
        mostrarNotas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    else:
        print('FINALIZANDO...')
        break
print('<<< VOLTE SEMPRE >>>')

    

