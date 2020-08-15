# Crie um pacote chamado utilidadesCeV que tenha 2 módulos internos chamados "moeda" e "dado". 
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

import utilidadesCeV.moeda

preco = float(input('Digite um preço: R$ '))
utilidadesCeV.moeda.resumo(preco, True)