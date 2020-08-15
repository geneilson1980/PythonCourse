# Criem um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista la dentro ele não deve ser adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente.

valores = []

while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
        continuar = str(input('Quer continuar? [S/N]' ))
        if continuar in 'nN':
            break
    else:
        print('Valor duplicado! Não vou adicionar')
        continuar = str(input('Quer continuar? [S/N]' ))
        if continuar in 'nN':
            break
print('-=' * 40)
print(f'Você digitou os valores {sorted(valores)}')