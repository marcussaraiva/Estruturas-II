from nodeArvoreBinaria import *
from arvoreBinaria import *

def main():
# Criando Raiz #
    raiz = NodeArvoreBinaria(0)
# Criando Nós #
    node1 = NodeArvoreBinaria(1)
    node2 = NodeArvoreBinaria(2)
    node3 = NodeArvoreBinaria(3)
    node4 = NodeArvoreBinaria(4)
    node5 = NodeArvoreBinaria(5)
    node6 = NodeArvoreBinaria(6)
    node7 = NodeArvoreBinaria(7)
    node8 = NodeArvoreBinaria(8)
    node9 = NodeArvoreBinaria(9)
    node10 = NodeArvoreBinaria(10)
# Inserindo Nós #
    raiz.esquerda = node1
    raiz.direita = node2
    node1.esquerda = node3
    node1.direita = node4
    node2.esquerda = node5
    node2.direita = node6
    node5.esquerda = node7
    node5.direita = node8
    node7.esquerda = node9
    node8.direita = node10
# Instanciando Arvore #
    arvore_binaria = ArvoreBinaria(raiz)

    # print(arvore_binaria.tamanho())
    print("Antes de espelhar:")
    arvore_binaria.mostrar_largura(raiz)
    arvore_binaria.espelhar()
    print("\nDepois de espelhar:")
    arvore_binaria.mostrar_largura(raiz)
    # print(arvore_binaria.contar_folhas())
    # arvore_binaria.arvore_cheia()


if __name__ == "__main__":
    main()