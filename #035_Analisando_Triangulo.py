# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

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
    print("Estes 3 segmentos podem formar um triângulo") 
else:
    print("Estes 3 segmentos NÃO podem formar um triângulo") 