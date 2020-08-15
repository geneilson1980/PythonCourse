# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.

kmPercorrido = float(input('Qual foi a quantidade de KM percorridos pelo carro?' ))
qtdDias = int(input('Digite a quantidade de dias que o carro ficou alugado: '))
precoDiaria = 60
precoKmRodado = 0.15
precoPagar = (qtdDias * precoDiaria) + (kmPercorrido * precoKmRodado)

print(f'O preço a pagar pelo aluguel do carro é R${precoPagar:.2f} reais!')