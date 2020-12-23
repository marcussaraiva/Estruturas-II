#
# ÁREA DESTINADA A IMPLEMENTAÇÃO
#
from deque import *

def main():
    deque = Deque(10)
    deque.inserir_final(4)
    deque.inserir_final(1)
    deque.inserir_final(2)
    deque.inserir_final(5)
    deque.inserir_final(3)
    deque.inserir_final(8)
    deque.inserir_final(0)
    deque.inserir_final(6)
    deque.inserir_final(9)
    deque.inserir_final(7)
#    deque.inserir_inicio("Pri")
#    deque.inserir_inicio("Seg")
#    deque.inserir_inicio("Ter")
#    deque.inserir_final("Final")
    deque.mostrar()
#    deque.remover_inicio()
#    deque.remover_final()
#    deque.remover_por_indice(0)
    deque.ordenar()
    deque.mostrar()
    deque.get_tamanho()

if __name__ == "__main__":
    main()