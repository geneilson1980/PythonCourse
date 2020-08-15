#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de ZERO até VINTE

#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

numerosExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
                  'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
                  'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 
                  'dezessete', 'dezoito', 'dezenove', 'vinte')
cont = len(numerosExtenso)

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if numero >= 0 and numero < cont:
        print(f'Você digitou o número {numerosExtenso[numero]}')
        break
    else:
        print(f'Você digitou o número {numero}. Por favor, digite um número entre 0 e 20!')
