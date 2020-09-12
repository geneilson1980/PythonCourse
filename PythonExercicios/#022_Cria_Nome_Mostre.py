# Crie um programa que leia o nome completo de uma pessoa e mostre:
# --> O nome com todas as letras MAIÚSCULAS e minúsculas
# --> Quantas letras ao todo (sem considerar os espaços)
# --> Quantas letras tem o primeiro nome
import string


nomeCompleto = input(str('Digite seu nome completo: '))
nomeMaiusculo = nomeCompleto.upper()
nomeMinusculo = nomeCompleto.lower()
qtdLetrasGeral = len(nomeCompleto) -nomeCompleto.count(' ')
splitPName = nomeCompleto.split(' ')
qtdLetrasPName = len(splitPName[0])

print(f'O seu nome em UpperCase é: {nomeMaiusculo}')
print(f'O seu nome em LowerCase é: {nomeMinusculo}')
print(f'O seu nome completo tem {qtdLetrasGeral} letras')
print(f'O seu primeiro nome tem {qtdLetrasPName} letras')
