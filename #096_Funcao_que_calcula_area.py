# Faça um programa que tenha uma função chamada área() que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    mult = l * c
    return mult


print('Controle de Terrenos')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

result = area(largura, comprimento)

print(f'A área de um terreno de {largura}x{comprimento} é de {result}m².') #alt+0178