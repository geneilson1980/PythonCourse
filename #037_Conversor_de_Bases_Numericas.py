# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para BINÁRIO
# - 2 para OCTAL
# - 3 para HEXADECIMAL

numero = int(input('Digite um número inteiro: '))

print('Escolha umas das bases para conversão: ')
print('[ 1 ] converter para BINÁRIO') 
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')

opcao = int(input('Sua opção: '))

if opcao == 1:
    numTemp = bin(numero)
    numConvertido = numTemp[2:]
    # removing "0b" prefix
    base = 'BINÁRIO'
elif opcao == 2:
    numTemp = oct(numero)
    numConvertido = numTemp[2:]
    base = 'OCTAL'
else:
    numTemp = hex(numero)
    numConvertido = numTemp[2:]
    base = 'HEXADECIMAL'

print(f'O número {numero} convertido para {base} é igual a {numConvertido}')