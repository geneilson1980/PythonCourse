#Escreva um programa que converta uma temperatura digitada em Celcius e converta para Fahrenheit
temperatura = float(input("Digite a temperatura em Celcius que deseja converter para Fahrenheit: "))
factorF = 1.8
baseF = 32
fahrenheit = (temperatura * factorF) + baseF

print('\n','='*20)
print(f'A temperatura de {temperatura} graus Celcius é equivalente a {fahrenheit:.1f} graus Fahrenheit!')
print('='*20)