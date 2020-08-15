# # crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

parenteses = []

expressao = str(input('Digite a expressão: '))
expressaoSize = len(expressao)
contLeft = 0
contRight = 0

for x in range(expressaoSize):
    word = expressao[x]
    if word in '()':
        parenteses.append(word)
        if word == '(':
            contLeft += 1
        else:
            contRight += 1
if contLeft == contRight:
    print(f'Sua expressão "{parenteses}" está válida')
else:
    print(f'Sua expressão "{parenteses}" não é válida, nós temos {contLeft} parenteses abertos e {contRight} parenteses fechaods')