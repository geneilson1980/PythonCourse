# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alunos = ["Jose", "Maria", "Pedro", "Joana", "Cleide", "Marcos"]

print('\n')
print('='*20)
print('A ordem de apresentação dos trabalhos será pela ordem: ')
random.shuffle(alunos)
print(alunos)
print('='*20)