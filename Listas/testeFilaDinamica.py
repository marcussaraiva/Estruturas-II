#
# ÁREA DESTINADA A IMPLEMENTAÇÃO
#
from filaDinamica import *
from node import *

def main():
    filaDinamica = FilaDinamica()
    filaDinamica.inserir(2)
    filaDinamica.inserir(3)
    #filaDinamica.inserir(4)
    #filaDinamica.inserir(5)
    filaDinamica.mostrar()

if __name__ == "__main__":
    main()