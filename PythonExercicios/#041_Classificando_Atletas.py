# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria de acordo com a idade:
# Até 9 anos: MITIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

import datetime

anoNAscimento = int(input("Digite o ano de seu nascimento: "))
idade = datetime.datetime.now().year - anoNAscimento

if idade <= 9:
    print(f'O atleta tem {idade} anos.')
    print('CLASSIFICAÇÃO: MIRIM')
elif idade <= 14:
    print(f'O atleta tem {idade} anos.')
    print('CLASSIFICAÇÃO: INFANTIL')
elif idade <= 19:
    print(f'O atleta tem {idade} anos.')
    print('CLASSIFICAÇÃO: JÚNIOR')
elif idade <= 25:
    print(f'O atleta tem {idade} anos.')
    print('CLASSIFICAÇÃO: SÊNIOR')
else:
    print(f'O atleta tem {idade} anos.')
    print('CLASSIFICAÇÃO: MÁSTER')