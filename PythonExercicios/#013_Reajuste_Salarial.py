# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salario com 15% de aumento

salarioFunc = float(input("Digite o salário atual do funcionário: "))
fatorAumento = 15
novoSalario = salarioFunc + ((salarioFunc / 100) * fatorAumento)

# Print "=" x vezes
print('='*20)
print("O salário atual do funcionário é R$ {:.2f} reais e com o aumento de {}% ele irá passar a receber R$ {:.2f} reais!".format(salarioFunc, fatorAumento, novoSalario))
print('='*20)
