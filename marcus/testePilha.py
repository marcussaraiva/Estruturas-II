from pilha import *
from time import sleep

def main():
    pilha = Pilha(10)
    pilha.inserir("Maria")
    pilha.mostrar()
    pilha.mostrar_topo()
    pilha.remover()

if __name__ == "__main__":
    main()