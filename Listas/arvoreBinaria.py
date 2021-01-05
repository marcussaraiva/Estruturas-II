from nodeArvoreBinaria import *
from pilha import *


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

    def tamanho(self, node=None):
        if node is None:
            node = self.raiz
        esquerda    = 0
        direita     = 0
        if node.esquerda:
            esquerda    = self.tamanho(node.esquerda)
        if node.direita:
            direita     = self.tamanho(node.direita)
        if esquerda > direita:
            return esquerda + 1
        return direita + 1

    def contar_folhas(self, node=None):
        if node is None:
            node = self.raiz
        contador = 0
        fila = []
        fila.append(node)
        while len(fila):
            node = fila.pop()
            if node.esquerda:
                fila.append(node.esquerda)
            if node.direita:
                fila.append(node.direita)
            if node.esquerda is None and node.direita is None:
                contador += 1
        return contador
      
    def arvore_cheia(self, node= None):
        if node is None:
            node = self.raiz
        tamanho = self.tamanho()
        total_de_nos = 2 ** (tamanho - 1)
        total_de_folhas = self.contar_folhas()
        if total_de_nos == total_de_folhas:
            return print("Árvore cheia!")
        return print("Árvore não cheia!")
    
    def espelhar(self, node=None):
        if node is None:
            node = self.raiz
        fila = []
        fila.append(node)
        while len(fila):
            node = fila.pop()
            if node:
                node.esquerda, node.direita = node.direita, node.esquerda
                fila.append(node.esquerda)
                fila.append(node.direita)
        return self.raiz