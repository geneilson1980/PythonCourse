# Reescreva a função "leiaInt()" que fizemos no desafio 104 incluindo agora a possibilidade da digitação de uma número de tipo inválido. Aproveite e crie também uma função "leiaFloat()" com a mesma funcionalidade.

# try:
# except Exception as erro:
# else: (optional)
# finally: (optional)

def leiaInt(msg):
    while True:       
        try:
            n = int(input(msg))
        except (ValueError, TypeError):        
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:       
        try:
            n = float(input(msg))
        except (ValueError, TypeError):        
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return n

n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o valor real foi {n2}')