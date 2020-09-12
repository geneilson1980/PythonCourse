#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostra a mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.

#Ex.: MULTDADO! Você excedeu o limite permitido que é de 80km/h
# Você deve pagar uma multa de R$280,00
# Tenha um bom dia! Dirija com segurança!

#cores no python
import math
import colored
velocidade = float(input('Digite a velocidade do carro: '))
velocidadeLimite = 80

if velocidade >= 81:
    tempNumber = math.modf(velocidade)
    velocidadeInteira = tempNumber[1]
    velocidadeAdicional = velocidadeInteira - velocidadeLimite
    print(colored.stylize('MULTADO! Você excedeu o limite permitido que é de 80km/h', colored.fg('red')))
    valorMulta = velocidadeAdicional * 7 
    print(colored.stylize(f'Você deve pagar uma multa de R${valorMulta}', colored.fg('red')))
    print(colored.stylize('Tenha um bom dia! Dirija com segurança!', colored.fg('yellow')))