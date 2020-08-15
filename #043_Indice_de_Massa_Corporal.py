# Desenvolva uma lógica que leia a altura e o peso de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
# Abaixo de 18.5: abaixo do peso
# Entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade morbida

altura = float(input('Digite a sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / pow(altura, 2)

print(f'O seu IMC é {imc:.1f}')

if imc < 18.5:
    print('Você está abaixo do seu peso ideal')
elif imc >= 18.5 and imc < 25:
    print('Você está no seu peso ideal')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Você está com obesidade')
else:
    print('Você está com obesidade morbida')