#Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.

primeiroValor = int(input("Digite o primeiro valor: "))
segundoValor = int(input("Digite o segundo valor: "))
terceiroValor = int(input("Digite o terceiro valor: "))

if primeiroValor < segundoValor and primeiroValor < terceiroValor:
    print(f"O menor valor digitado foi {primeiroValor}")
elif segundoValor < primeiroValor and segundoValor < terceiroValor:
    print(f"O menor valor digitado foi {segundoValor}")
elif terceiroValor < primeiroValor and terceiroValor < segundoValor:
    print(f"O menor valor digitado foi {terceiroValor}")

if primeiroValor > segundoValor and primeiroValor > terceiroValor:
    print(f"O maior valor digitado foi {primeiroValor}")
elif segundoValor > primeiroValor and segundoValor > terceiroValor:
    print(f"O maior valor digitado foi {segundoValor}")
elif terceiroValor > primeiroValor and terceiroValor > segundoValor:
    print(f"O maior valor digitado foi {terceiroValor}")