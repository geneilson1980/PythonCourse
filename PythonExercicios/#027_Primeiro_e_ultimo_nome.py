# Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome separadamente
#ex. Ana Maria de Souza
#saida
#Muito prazer em te conhecer
#seu primeiro nome é maria
#seu último nome é souza

nomeCompleto = input(str('Digite seu nome completo: '))
splitNome = nomeCompleto.split(' ')
primeiroNome = splitNome[0]
lastNome = splitNome[-1]

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {primeiroNome}')
print(f'Seu último nome é {lastNome}')