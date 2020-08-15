# Crie um programa que leia:
# nome, 
# ano de nascimento e 
# carteira de trabalho.

# Cadastre-os(com idade) em um dicionário. 

# Se por acaso a CTPS for difernte de ZERO, o dicionário receberá também:
# o ano de contratação e 
# o salário. 

# calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
import datetime
trabalhador = {}
nome = str(input('Nome: '))
trabalhador['nome'] = nome
sexo = str(input('sexo (M/F): '))
trabalhador['sexo'] = sexo
nascimento = int(input('Ano de nascimento: '))
trabalhador['nascimento'] = nascimento
idade = datetime.datetime.now().year - nascimento
trabalhador['idade'] = idade
ctps = int(input('Carteira de Trabalho (0 não tem): '))
trabalhador['ctps'] = ctps
if ctps != 0:
    anoContratacao = int(input('Ano de contratação: '))
    trabalhador['anocontratacao'] = anoContratacao
    salario = float(input('Salário: '))
    trabalhador['salario'] = salario
    if trabalhador['sexo'] in 'mM':
        tempoServico = datetime.datetime.now().year - anoContratacao
        aposentadoria = (35 - tempoServico) + idade
        trabalhador['aposentadoria'] = aposentadoria
    else:
        tempoServico = datetime.datetime.now().year - anoContratacao
        aposentadoria = (30 - tempoServico) + idade
        trabalhador['aposentadoria'] = aposentadoria
    print('-=' * 40)
    print(f'- O nome do trabalhador é: {trabalhador["nome"]}')
    print(f'- A idade do trabalhador é: {trabalhador["idade"]} anos')
    print(f'- O número da carteira de trabalho do trabalhador é: {trabalhador["ctps"]}')
    print(f'- A contratação ocorreu no ano de: {trabalhador["anocontratacao"]}')
    print(f'- O salário tem o valor de: R$ {trabalhador["salario"]}')
    print(f'- Essa pessoa vai se aposentar com {trabalhador["aposentadoria"]} anos')
if trabalhador['ctps'] == 0:
    print('-=' * 40)
    print(f'- O nome do trabalhador é: {trabalhador["nome"]}')
    print(f'- A idade do trabalhador é: {trabalhador["idade"]} anos')
    print(f'- O número da carteira de trabalho do trabalhador é: {trabalhador["ctps"]}')
