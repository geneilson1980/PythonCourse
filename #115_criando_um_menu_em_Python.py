# Crie um pequeno "sistema modularizado" que permita cadastrar pessoas pelo seu "nome" e "idade" em um arquivo de texto simples.

# O sistema só vai ter 2 opções:
#   - Cadastrar uma nova pessoa
#   - Listar todas as pessoas cadastradas.

import sisCadPkg.menu

nomeArquivo = 'arquivo_curso_em_video.txt'
if sisCadPkg.menu.verificaArquivo(nomeArquivo):
    print(f'O aquivo {nomeArquivo} já está criado!')
else:
    print(f'O aquivo {nomeArquivo} não existe! Vamos criá-lo...')
    criarArquivo = sisCadPkg.menu.createFile(nomeArquivo)
    if criarArquivo:
        print(f'O arquivo {nomeArquivo} foi criado com sucesso!')
    else:
        print(f'O arquivo {nomeArquivo} não foi criado!')

print(sisCadPkg.menu.linha())
print(sisCadPkg.menu.titulo())
print(sisCadPkg.menu.linha())
print(sisCadPkg.menu.menu('Sua Opção: ', nomeArquivo))