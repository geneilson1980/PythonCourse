import os.path

def menu(msg, arquivo):
    opcoes = {'1': '- Ver pessoas cadastradas', '2': '- Cadastrar nova pessoa', '3': '- Sair do Sistema'}
    while True:
        for i in opcoes:
            print(i, opcoes[i])
        escolha = str(input(msg))
        escolhaIsNumber = escolha.isdigit()
        if escolhaIsNumber:
            escolha = int(escolha)
        if (escolhaIsNumber) and (escolha == 1 or escolha == 2 or escolha == 3):
            if escolha == 1:
                print(linha())
                print('PESSOAS CADASTRADAS'.center(42))
                print(linha())
                lerPCadastradas = open(arquivo, 'r')
                cadastros = lerPCadastradas.readlines()
                for i in cadastros:
                    # The "b" variable is necessary to remove "\n" character of each line of file.
                    b = i[0:-1]
                    print(f'{b.split(";")[0]:<10}', end='')
                    print(f'{b.split(";")[1]:>20} anos')
                print(linha())
                print(titulo())
                print(linha())
                continue
            elif escolha == 2:
                print(linha())
                print('NOVO CADASTRO'.center(42))
                print(linha())
                nome = str(input('Nome: '))
                idade = str(input('Idade: '))
                with open(arquivo, 'a') as myFile:
                    myFile.write(f'{nome};')
                    myFile.write(f'{idade}\n')
                    print(f'O registro de {nome} foi adicionado ao sistema!')
                    print(linha())
                    print(titulo())
                    print(linha())
            else:
                print(linha())
                print('SAIR DO SISTEMA'.center(42))
                print(linha())
                print('Saindo do sistema. Obrigado!')
                print(linha())
                exit()
        elif (escolhaIsNumber) and (escolha == 0 or escolha >= 4):
            print('\033[0;31mERRO! Digite uma opção válida.\033[m')
            print(linha())
            print(titulo())
            print(linha())
            continue
        else:
            print('\033[0;31mERRO! Digite um número inteiro dentro das opções.\033[m')
            print(linha())
            print(titulo())
            print(linha())
            continue

def linha(tam = 40):
    ln = '-' * tam
    # return '-' * tam
    return ln

def titulo():
    tit = 'MENU PRINCIPAL'.center(42)
    return tit

def verificaArquivo(name):
    try:
        a = open(name)
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def createFile(name):
    try:
        arquivo = open(name, 'a')
        arquivoCriado = os.path.isfile(name)
    except FileNotFoundError:
        return False
    else:        
        return True


# print(linha())
# print(titulo())
# print(linha())

# # test = menu('Sua Opção: ')
# print(menu('Sua Opção: '))


