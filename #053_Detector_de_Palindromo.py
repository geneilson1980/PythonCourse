# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo desconsiderando os espaços.
#Ex.:
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

frase = str(input('Digite uma frase para verificar se ela é um palíndromo: '))
removeSpace = frase.replace(' ', '')
# reverseFrase = removeSpace[::-1]
reverseFrase = ''
# conta o total de strings -1 (0 até total -1, vai até -1 que menor que 0 (início), e vem contando -1)
for letra in range(len(removeSpace) -1, -1, -1):
    reverseFrase += removeSpace[letra]

if removeSpace == reverseFrase:
    print(f'A frase {frase} é um palíndromo {removeSpace} = {reverseFrase}')
else:
    print(f'A frase {frase} não é um palíndromo {removeSpace} =/= {reverseFrase}')