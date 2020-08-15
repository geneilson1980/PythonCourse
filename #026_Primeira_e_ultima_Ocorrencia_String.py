#Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = input(str('Digite uma frase: '))
x = frase.upper()
qtdA = 'A' in x
count = 0

for i in x:
    if i == 'A':
        count = count + 1


if count == 0:
    print('Não existe a letra "A" nesta frase!')
else:
    print(f'Existem {count} letra(s) "A" nesta frase!')

firstPosition = x.find('A')
print(f'A letra A aparace pela primeira vez na posição {firstPosition}')

lastPosition = x.rfind('A')
print(f'A letra A aparace pela última vez na posição {lastPosition}')