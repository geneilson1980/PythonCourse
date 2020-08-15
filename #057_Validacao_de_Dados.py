#Faça um programa que leia o sexo de uma pessoa mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter o valor correto.

sexo = str(input('Infomre seu sexo: [M/F] ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]

if sexo in 'MmFf':
    print(f'Sexo {sexo} registrado com sucesso')
