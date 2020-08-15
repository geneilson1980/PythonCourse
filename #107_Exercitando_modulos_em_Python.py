# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
import modulos.moeda

preco = float(input('Digite um preço: R$ '))
print(f'A metade de R$ {preco} é R$ {modulos.moeda.diminuir(preco)}')
print(f'O dobro de R$ {preco} é R$ {modulos.moeda.dobro(preco)}')
print(f'Aumentando 10% de R$ {preco} temos R$ {modulos.moeda.aumentar(preco)}')