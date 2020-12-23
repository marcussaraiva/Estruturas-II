#
# ÁREA DESTINADA A IMPLEMENTAÇÃO
#
from dequeDinamico import *
from node import Node

def main():
    dequeDinamico = DequeDinamico()
    dequeDinamico.inserir_inicio("Pri")
#    dequeDinamico.inserir_inicio("Seg")
#    dequeDinamico.inserir_inicio("Ter")
#    dequeDinamico.inserir_final("Final")
    dequeDinamico.mostrar()
    dequeDinamico.get_tamanho()
#    dequeDinamico.remover_inicio()
#    dequeDinamico.remover_final()
    dequeDinamico.reinicializar()
    dequeDinamico.mostrar()
    dequeDinamico.get_tamanho()

if __name__ == "__main__":
    main()