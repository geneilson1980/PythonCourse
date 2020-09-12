#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
#presta atencão na precedencia

nota1 = int(input('Digite a sua nota 1: '))
nota2 = int(input('Digite a sua nota 2: '))
media = float((nota1 + nota2) / 2)

print('A média das notas {} e {} é: {}'.format(nota1, nota2, media))