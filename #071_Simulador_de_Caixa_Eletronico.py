#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual o valor a ser sacado (número inteiro) e o programa irá informar quantas cédulas de cada valor serão entregues.

#Obs: Considere quye oc aixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 40)
print(' '* 15, 'BANCO CEV')
print('=' * 40)
saque = int(input('Que valor você quer sacar? R$ '))
cont50 = 0
cont20 = 0
cont10 = 0
cont1 = 0

while True:
    if saque >= 50:
        cont50+=1
        saque = saque - 50
    elif saque >= 20:
        cont20 += 1
        saque = saque - 20
    elif saque >= 10:
        cont10 += 1
        saque = saque - 10
    elif saque >= 1:
        cont1 += 1
        saque = saque - 1
    else:
        break
if cont50 != 0:
    print(f'Total de {cont50} cédulas de R$50')
if cont20 != 0:
    print(f'Total de {cont20} cédulas de R$20')
if cont10 != 0:
    print(f'Total de {cont10} cédulas de R$10')
if cont1 != 0:
    print(f'Total de {cont1} cédulas de R$1')
print('=' * 40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia')

    
    
