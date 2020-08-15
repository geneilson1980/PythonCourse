# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa. 

# O quadrado da hipotenusa é igual a soma dos quadrados dos catetos (Veja módulo math)

catetoOposto = int(input("Digite o valor do cateto oposto:"))
expCatetoOposto = pow(2,catetoOposto)
catetoAdjacente = int(input("Digite o valor do cateto adjacente:"))
expCatetoAdjacente = pow(2,catetoAdjacente)
hipotenusa = expCatetoOposto + expCatetoAdjacente

if (pow(2,catetoOposto) + pow(2,catetoAdjacente) == hipotenusa):
    print("O valor do quadrado do cateto oposto é {}".format(expCatetoOposto))
    print("O valor do quadrado do cateto adjacente é {}".format(expCatetoAdjacente))
    print("O valor do quadrado da hipotenusa é {}".format(hipotenusa))
    print("O triangulo é um triângulo retângulo")
else:
    print("O triangulo não é um triângulo retângulo")