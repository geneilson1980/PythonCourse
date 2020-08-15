# Crie um programa que leia dois valores e mostre um menu como o abaixo:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# Se o usuário digitar uma opção inválida, informe e repita o menu

# Seu programa deverá realizar a operação solicitada em cada caso

primerioValor = int(input('Digite o primeiro valor: '))
segundoValor = int(input('Digite o segundo valor: '))
opcao = 0

print('     [1] Somar')
print('     [2] Multiplicar')
print('     [3] Maior')
print('     [4] Novos números')
print('     [5] Sair do programa')

opcao = int(input('>>>>> Qual a sua opção? '))

while opcao != 5:
    if opcao == 1:
        print(f'A soma entre {primerioValor} + {segundoValor} é {primerioValor + segundoValor}')
        print('=-='*10)
        break
    elif opcao == 2:
        print(f'A multiplicação entre {primerioValor} e {segundoValor} é {primerioValor * segundoValor}')
        print('=-='*10)
        break
    elif opcao == 3:
        if primerioValor > segundoValor:
            print(f'O maior valor é {primerioValor}')
            print('=-='*10)
            break
        elif primerioValor < segundoValor:
            print(f'O maior valor é {segundoValor}')
            print('=-='*10)
            break
        elif primerioValor == segundoValor:
            print(f'Os 2 valores são iguais a {primerioValor}')
            print('=-='*10)
            break
    elif opcao == 4:
        primerioValor = int(input('Digite um novo primeiro valor: '))
        segundoValor = int(input('Digite um novo segundo valor: '))
        print('     [1] Somar')
        print('     [2] Multiplicar')
        print('     [3] Maior')
        print('     [4] Novos números')
        print('     [5] Sair do programa')
        opcao = int(input('>>>>> Qual a sua opção? '))
    else:
        print('Opção inválida. Tente novamente!')
        print('     [1] Somar')
        print('     [2] Multiplicar')
        print('     [3] Maior')
        print('     [4] Novos números')
        print('     [5] Sair do programa')
        opcao = int(input('>>>>> Qual a sua opção? '))
        print('=-='*10)

print('Finalizando...')
print('Fim do programa, volte sempre!')
print('=-='*10)