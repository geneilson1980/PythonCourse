# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$50.50 por KM para viagens de até 200KM e R$0,45 para viagnes mais longas
import math

distanciaViagem = float(input('Digite a distância da viagem em KM: '))
distanciaBase = 200
precoPassagem1 = float(0.50)
precoPassagem2 = float(0.45)
desconto = precoPassagem1-precoPassagem2
valorPassagem= 0

if distanciaViagem <= distanciaBase:
    valorPassagem = distanciaViagem * precoPassagem1
    print(f'O valor da passagem é: R${valorPassagem}')
else:
    valorPassagem = distanciaViagem * precoPassagem2
    print(f'O valor da passagem tem desconto e o valor final  é: R${valorPassagem}')