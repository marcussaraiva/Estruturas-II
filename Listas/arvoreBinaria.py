from nodeArvoreBinaria import *

class ArvoreBinaria:
    def __init__(self, node):
        self.raiz = node
    
    def mostrar_largura(self, node):
        if node is self.raiz:
            print(node, " | ", end='')
        if node.esquerda:
            print(node.esquerda, " | ", end='')  
        if node.direita:
            print(node.direita, " | ", end='')
        if node.esquerda:
            self.mostrar_largura(node.esquerda)
        if node.direita:
            self.mostrar_largura(node.direita)