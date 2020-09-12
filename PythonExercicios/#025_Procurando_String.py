# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

nome = input(str("Digite o seu nome: "))
x = nome.lower()
nomeDesejado = 'silva' in x

if nomeDesejado:
    if x[:5] == 'silva':
        print('O seu nome começa com "SILVA"')
    else:
        print('O seu nome contém "SILVA" mas ele nao está no início do nome')
else:
    print('O seu nome NÃO contém "SILVA"')