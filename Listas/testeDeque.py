#
# ÁREA DESTINADA A IMPLEMENTAÇÃO
#
from deque import *

def main():
    deque = Deque(5)
    deque.inserir_inicio("Pri")
    deque.inserir_inicio("Seg")
    deque.inserir_inicio("Ter")
    deque.inserir_final("Final")
    deque.mostrar()
    deque.remover_inicio()
    deque.remover_final()
    deque.remover_por_indice(0)
    deque.mostrar()

if __name__ == "__main__":
    main()