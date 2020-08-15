# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = input(str("Digite um nome de cidade: "))
x = cidade.lower()
nomeDesejado = 'santo' in x

if nomeDesejado:
    if x[:5] == 'santo':
        print('O nome da cidade começa com "SANTO"')
    else:
        print('O nome da cidade contém o nome "SANTO" mas ele nao está no início do nome')
else:
    print('O nome da cidade NÃO contém "SANTO"')