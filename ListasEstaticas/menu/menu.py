#
#   AREA DE MENU PARA SER IMPLEMENTADA POSTERIORMENTE
#
from interface import menu,cabecalho
from time import sleep

while True:
    resposta = menu([   'Inserir',
                        'Remover',
                        'Imprimir',
                        'Sair'  ])
    if resposta == 1:   cabecalho('Inserir')
    elif resposta == 2: cabecalho('Remover')
    elif resposta == 3: cabecalho('Imprimir')
    elif resposta == 4: 
        cabecalho('Programa Finalizado') 
        break 
    else:
        print('\n\033[31mErro: digite uma opção válida!\033[m')
    sleep(1)