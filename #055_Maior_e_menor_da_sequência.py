# Faça um programa que leia o peso de cinco pessoas, no final, mostre qual foi o maior e o menor peso lidos.

pesos = []
pesoMaior = 0
pesoMenor = pesoMaior
for peso in range(1, 6):
    numero = float(input(f'Digite o peso da {peso}ª pessoa: '))
    pesos.append(numero)

print(pesos)

n = len(pesos)
# Percorre todos os elementos da lista
for i in range(n):
    # Os últimos elementos i já estão no lugar
    for j in range(0, n-i-1):
        # Percorre a lista de 0 até n-i-1
        # Troca o elemento de lugar se ele for maior que o próximo elemento
        if pesos[j] > pesos[j+1]:
            pesos[j], pesos[j+1] = pesos[j+1], pesos[j]

print(pesos)

print(f'O maior peso encontrado foi {pesos[n-1]}')
print(f'O menor peso encontrado foi {pesos[0]}')