# Crie um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (Opcional)
# - Adicione também as docstrings.

def notas(*qtdNotas, sit=False):
    """
        - Quantidade de notas
        - A maior nota
        - A menor nota
        - A média da turma
        - A situação (Opcional)
        - Adicione também as docstrings.
    """
    notasTurma = {}
    maior = qtdNotas[0]
    menor = qtdNotas[0]
    notasTurma['maior'] = maior
    notasTurma['menor'] = menor
    somaNotas = 0
    media = 0
    j = 1
    for i in qtdNotas:
        notasTurma['total'] =+ j
        if i > maior:
            maior = i
            notasTurma['maior'] = maior
        if i < menor:
            menor = i
            notasTurma['menor'] = menor
        somaNotas += i
        j += 1
    media = somaNotas / len(qtdNotas)
    notasTurma['media'] = media
    if sit == True:
        if media < 5:
            notasTurma['situacao'] = 'RUIM'
        elif media < 7:
            notasTurma['situacao'] = 'REGULAR'
        elif media < 9:
            notasTurma['situacao'] = 'BOA'
        else:
            notasTurma['situacao'] = 'EXCELENTE'
    
    return notasTurma
            
resp = notas(5.5, 6.5, 7.5, 9.8, sit=True)
print(resp)
# help(notas)