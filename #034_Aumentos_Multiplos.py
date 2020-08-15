# Escreva um programa que pergunte um salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%
# Para salários inferiores ou iguais, o aumento é de 15%

salario = float(input("Digite o valor do seu salário: "))

if salario > 1250:
    novoSalario = (salario / 100) * 10 + salario
    print(f"Você recebeu um aumento de 10% e seu novo salário é de: R${novoSalario:.2f}")
else:
    novoSalario = (salario / 100) * 15 + salario
    print(f"Você recebeu um aumento de 15% e seu novo salário é de: R${novoSalario:.2f}")