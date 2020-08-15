# Adapte o código do desafio 107 criando uma função adicional chamada moeda() que consgia mostrar os valores como um valor monetário formatado.

import modulos.moeda

preco = float(input('Digite um preço: R$ '))
print(f'A metade de {modulos.moeda.moeda(preco)} é {modulos.moeda.diminuir(preco)}')
print(f'O dobro de {modulos.moeda.moeda(preco)} é {modulos.moeda.dobro(preco)}')
print(f'Aumentando 10% de {modulos.moeda.moeda(preco)} temos {modulos.moeda.aumentar(preco)}')