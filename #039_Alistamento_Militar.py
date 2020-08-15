# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade se ele AINDA VAI SE ALISTAR ao serviço militar, se É A HORA DE SE ALISTAR ou se JÁ PASSOU O TEMPO de alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

import datetime
anoNascimento = int(input('Digite o ano do seu nascimento: '))
idade = datetime.datetime.now().year - anoNascimento

if idade < 18:
    diferenca = 18 - idade
    print(f'Quem nasceu em {anoNascimento} tem {idade} anos em {datetime.datetime.now().year}')
    print(f'Ainda faltam {diferenca} para o alistamento')
    print(f'Seu alistamento será em {datetime.datetime.now().year + diferenca}')
elif idade == 18:
    print(f'Quem nasceu em {anoNascimento} tem {idade} anos em {datetime.datetime.now().year}')
    print(f'Você tem que se alistar IMEDIATAMENTE!')
else:
    diferenca = idade - 18
    print(f'Quem nasceu em {anoNascimento} tem {idade} anos em {datetime.datetime.now().year}')
    print(f'Já se passaram {diferenca} anos do seu alistamento obrigatório')
