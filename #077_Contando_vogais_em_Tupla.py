# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar para cada palavra, quais são as suas vogais.

vogais = ('A', 'E', 'I', 'O', 'U')
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for palavra in palavras:
    palavraSize = len(palavra)
    print(f'\nNa palavra {palavra} temos:', end=' ')
    for w in range(palavraSize):
        if palavra[w] in vogais:
            print(f'{palavra[w]}', end=' ')