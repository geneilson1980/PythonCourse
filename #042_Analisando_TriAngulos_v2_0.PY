# Refaça o desafio 035 dos triangulos acrescentando o recurso de mostrar que tipo de triangulo será formado:
# EQUILÁTERO: Todos os lados são iguais
# ISÓSCELES: 2 lados iguais
# ESCALENO: todos os lados são diferentes

retaA = float(input("Digite o comprimento da primeira reta: "))
retaB = float(input("Digite o comprimento da segunda reta: "))
retaC = float(input("Digite o comprimento da terceira reta: "))

formaTrianguloA = False
formaTrianguloB = False
formaTrianguloC = False

if abs(retaB - retaC) < retaA < (retaB + retaC):
    formaTrianguloA = True
if abs(retaA - retaC) < retaB < (retaA + retaC):
    formaTrianguloB = True
if abs(retaA - retaB) < retaC < (retaA + retaB):
    formaTrianguloC = True

if formaTrianguloA and formaTrianguloB and formaTrianguloC == True:
    if retaA == retaB and retaB == retaC:
        print("Estes 3 segmentos podem formar um triângulo")
        print("O tipo de trinângulo formado é: EQUILÁTERO")
    elif retaA == retaB or retaB == retaC or retaA == retaC:
        print("Estes 3 segmentos podem formar um triângulo")
        print("O tipo de trinângulo formado é: ISÓSCELES")
    else:
        print("Estes 3 segmentos podem formar um triângulo")
        print("O tipo de trinângulo formado é: ESCALENO") 
else:
    print("Estes 3 segmentos NÃO podem formar um triângulo") 