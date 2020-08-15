# Faça um programa que tenha uma função chamada escreva() que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex. 
#   escreva('Olá, Mundo!)
# Saída:
#   ~~~~~~~~~~~~~~~~~~~~~
#   Olá, Mundo!
#   ~~~~~~~~~~~~~~~~~~~~~

def escreva(text):
    textLen = len(text) + 4
    print('~' * (textLen))
    print(f'  {text}')
    print('~' * (textLen))


texto = str(input('Digite um texto: '))
escreva(texto)