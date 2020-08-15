#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m(2)

largura = float(input("Digite a largura em metros da parede:"))
altura = float(input("Digite a altura em metros da parede:"))
areaParede = largura * altura
qtdTinta = areaParede / 2

print("A sua parede tem {} metros de altura e {} metros de largura. A área total da sua parede é de {} metros quadrados e a quantidade de tinta necessária será de {} litros!".format(altura, largura, areaParede, qtdTinta))