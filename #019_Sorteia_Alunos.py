# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido

#veja ramdon

import random

alunos = ["Jose", "Maria", "Pedro", "Joana", "Cleide", "Marcos"]

print('\n')
print('='*20)
print(f"O aluno ou aluna escolhido(a) para apagar o quadro foi o de {random.choice(alunos)}!")
print('='*20)