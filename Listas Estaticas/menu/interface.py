#
#   AREA DE MENU PARA SER IMPLEMENTADA POSTERIORMENTE
#
def leia_resposta(resposta_usuario):
    while True:
        try:
            numero_resposta = int(input(resposta_usuario))
        except (ValueError, TypeError):
            print('\033[31mErro: digite uma opção válida!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário interrompeu manualmente!\033[m')
            print('\n\033[31mCaso queira sair, digite 4!\033[m')
            return 0
        else: return numero_resposta

def linha(tam=42):
    return '-' * tam

def cabecalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())

def menu(lista):
    cabecalho('Lista Linear')
    i = 1
    for item in lista:
        print(f'{i} - {item}')
        i+=1
    print(linha())
    resposta = leia_resposta('Resposta: ')
    return resposta