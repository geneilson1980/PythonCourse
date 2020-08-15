# crie um programa que leia o ano de nascimento de sete pessoas, no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
pessoas = []
maior = 0
menor = 0
for x in range(1, 8):
    pergunta = int(input(f'Em que ano a {x}ª pessoa nasceu? '))
    pessoas.append(pergunta)

for ano in range(len(pessoas)):
    idade = datetime.datetime.now().year - pessoas[ano]
    if idade >= 21:
        maior+= 1
    else:
        menor+= 1

print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também {menor} pessoas menores de idade')