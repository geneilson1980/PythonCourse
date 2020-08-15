# Crie um programa que tenha uma função fatorial() que receba 2 parâmetros: o primeiro que indique o número a calcular e o outro chamado "show" que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    """
        fatorial(n, show=False):
            -> Calcula o fatorial de um número.
            : param n: O número a ser calculado.
            : param show: (opcional) Mostrar ou não a conta
            : return: O valor do fatorial de um número n.
    """
    fatorial = 1
    if show:
        for i in range(n, 0, -1):
            fatorial = fatorial * i
            if i != 1:
                print(f'{i} x ', end='')
            else:
                print(f'{i} = ', end='')
            
        return fatorial
    else:
        for i in range(n, 0, -1):
            fatorial = fatorial * i
        return fatorial

fat = int(input('Digite um número para calcular seu fatorial: '))
mostrarProcesso = str(input('Deseja ver o processo de calculo sendo impresso na tela? [S/N] '))
if mostrarProcesso in 'sS':
    mostrarProcesso = True
else:
    mostrarProcesso = False

# help(fatorial)
# numFat = fatorial(fat, show=mostrarProcesso)
numFat = fatorial(fat)
if mostrarProcesso == True:
    print(numFat)
else:
    print(f'O fatorial de {fat} é: {numFat}')