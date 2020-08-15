# Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:
# à vista (dinheiro ou cheque): 10% de desconto
# à vista (cartão): 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print('========== LOJAS GUANABARA ==========')

precoCompras = float(input('Preço das compras: R$'))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] À vista com dinheiro/cheque')
print('[ 2 ] À vista com cartão de débito')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão de crédito')

formaPagamento = int(input('Digite o número da opção de pagamento: '))

if formaPagamento == 4:
    parcelas = int(input('Quantas parcelas: '))

if formaPagamento == 1:
    precoFinal = precoCompras - ((precoCompras / 100) * 10) 
    print(f'Sua compra de R${precoCompras:.2f} vai custar R${precoFinal:.2f} com o desconto de 10%') 
elif formaPagamento == 2:
    precoFinal = precoCompras - ((precoCompras / 100) * 5) 
    print(f'Sua compra de R${precoCompras:.2f} vai custar R${precoFinal:.2f} com o desconto de 5%')
elif formaPagamento == 3:
    precoFinal = precoCompras
    print(f'Sua compra vai custar R${precoFinal:.2f} porque não tem desconto')
else:
    precoFinal =  precoCompras + ((precoCompras / 100) * 20)
    valorParcelas = precoFinal / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${valorParcelas:.2f} COM JUROS')
    print(f'Sua compra de R${precoCompras:.2f} vai custar R${precoFinal:.2f} no final') 