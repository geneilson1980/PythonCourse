# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
import math

numero =  int(input('Digite um número: '))
dobro = 2 * numero
triplo = 3 * numero
# rQuadrada = int(math.sqrt(numero))
rQuadrada = math.sqrt(numero)

print('O número digitado foi {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}'.format(numero, dobro, triplo,rQuadrada))