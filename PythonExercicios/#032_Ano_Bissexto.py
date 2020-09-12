#AULA 10
#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

import datetime

ano = int(input("Digite um ano qualquer para verificar se ele é bissexto: "))
stringAno = str(ano)
last2NumbersAno = stringAno[-2:]
currentYear = datetime.datetime.now().year

if ano == 0:
    ano = currentYear

if (ano % 4) != 0:
    print(f"O ano {ano} não é BISSEXTO!")
elif (ano % 4) == 0 and last2NumbersAno == '00':
    if (ano % 400) == 0:
        print(f"O ano {ano} é BISSEXTO!")
    else:
        print(f"O ano {ano} não é BISSEXTO!")
elif (ano % 4) == 0:
    print(f"O ano {ano} é BISSEXTO!")