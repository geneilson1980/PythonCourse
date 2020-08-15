#Refaça o desafio 009 mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

numero = int(input('Digite um número para vermos a sua tabuada: '))

for x in range(1, 11):
    resultado = numero * x
    print(f'{numero} x {x} = {resultado}')
