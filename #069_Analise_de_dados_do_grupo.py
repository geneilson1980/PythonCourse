# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntar se o usuário quer o u não continuar. NO final, mostre:

# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados
# C) Quantas mulheres tem menos de 20 anos.

contIdade = 0
contHomens = 0
contMulheres = 0

while True:
    print('-' * 40)
    print('CADASTRE UMA PESSOA')
    print('-' * 40)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]')).upper()
    if idade > 18:
        contIdade+=1
    if sexo == 'M':
        contHomens+=1
    if sexo == 'F' and idade < 20:
        contMulheres+=1
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar != 'S':
        break

print(f'Total de pessoas com mais de 18 anos: {contIdade}')
print(f'Ao todo temos {contHomens} homem(ns) cadastrado(s)')
print(f'E temos {contMulheres} mulher(es) com menos de 20 anos')