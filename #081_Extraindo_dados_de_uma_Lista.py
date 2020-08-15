# Crie um prgrama que vai ler vários números colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados
# B) A lista de valores ordenada de forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
cont = 0
while True:
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    cont += 1
    continuar = str(input('Quer continuar? [S/N]' ))
    if continuar in 'nN':
        break
print('-=' * 40)
print(f'Você digitou {cont} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 foi inserido na lista')
else:
    print('O valor 5 não foi digitado')
