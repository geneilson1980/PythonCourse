# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda() desenvolvido no desafio 108. 

import modulos.moeda

preco = float(input('Digite um preço: R$ '))
print(f'A metade de {modulos.moeda.moeda(preco)} é {modulos.moeda.metade(preco, True)}')
print(f'O dobro de {modulos.moeda.moeda(preco)} é {modulos.moeda.dobro(preco, True)}')
print(f'Aumentando 10% de {modulos.moeda.moeda(preco)} temos {modulos.moeda.aumentar(preco, True)}')
print(f'Retirando 10% de {modulos.moeda.moeda(preco)} temos {modulos.moeda.diminuir(preco, True)}')