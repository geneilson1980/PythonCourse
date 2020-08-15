# Escreva um progrmama para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não poderá exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input("Digite o valor da casa: R$ "))
salarioComprador = float(input("Digite o seu salário: R$ "))
anosFinanciamento = int(input("Digite a quantidade de anos desejada para o financiamento: "))
prestacaoMensal = valorCasa / (anosFinanciamento * 12)
porcentagemSalario = (prestacaoMensal / salarioComprador) * 100

if porcentagemSalario <= 30:
    print(f"Para pagar uma casa de R${valorCasa:.2f} em {anosFinanciamento} anos, a prestação será de R${prestacaoMensal:.2f}")
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print(f'O valor da prestação vai comprometer {porcentagemSalario:.2f}% do seu salário, a porcentagem máxima é de 30%.')
    print("Empréstimo NÃO pode ser concedido!")