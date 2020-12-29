from arvore import*
from nodeArvore import*

def main():

    raiz = Node(0)
    arvore = Arvore(raiz)
# Criando Nós #
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    node11 = Node(11)
    node12 = Node(12)

# Inserindo Nós #
    # Raiz #
    raiz.inserir(node1)
    raiz.inserir(node2)
    raiz.inserir(node3)
    # Nó #
    node1.inserir(node4)
    node1.inserir(node5)
    node2.inserir(node6)
    node3.inserir(node7)
    node3.inserir(node8)
    node4.inserir(node9)
    node4.inserir(node10)
    node6.inserir(node11)
    node8.inserir(node12)

    """ arvore.mostrar_profundidade() """
    arvore.mostrar_largura()

if __name__ == "__main__":
    main()