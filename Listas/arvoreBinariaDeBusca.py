from nodeArvoreBinaria import *

class ArvoreBinariaBusca:

    def __init__(self, node=None, dado=0):
        if node:
            self.raiz = node
        elif dado:
            node = NodeArvoreBinaria(dado)
            self.raiz = node
        else:
            self.raiz = None

    def inserir(self, dado):
        pai = None
        i = self.raiz
        while(i):
            pai = i
            if dado < i.dado:
               i = i.esquerda
            else:
                i = i.direita
        if pai is None:
            self.raiz = NodeArvoreBinaria(dado)
        elif dado < pai.dado:
            pai.esquerda = NodeArvoreBinaria(dado)
        else:
            pai.direita = NodeArvoreBinaria(dado)
    
    def mostrar_largura(self, node=None):
        if node is None:
            node = self.raiz
        if node.esquerda:
            self.mostrar_largura(node.esquerda)
        print(node, " | ",end="")
        if node.direita:
            self.mostrar_largura(node.direita)
