from NodeArvRB import *

class ArvoreRB:
    def __init__(self):
        self.TNULL = NodeArvRB(0)
        self.TNULL.cor = 0
        self.TNULL.esquerda = None
        self.TNULL.direita = None
        self.raiz = self.TNULL

    def inserir(self, chave):
        node = Node(chave)
        node.pai = None
        node.dado = chave
        node.esquerda = self.TNULL
        node.direita = self.TNULL
        node.cor = 1
        pai_ = None
        auxiliar = self.raiz
        while auxiliar != self.TNULL:
            pai_ = auxiliar
            if node.dado < auxiliar.dado:
                auxiliar = auxiliar.esquerda
            else:
                auxiliar = auxiliar.direita
        node.pai = pai_
        if pai is None:
            self.raiz = node
        elif node.dado < pai.dado:
            pai.esquerda = node
        else:
            pai.direita = node
        if node.pai is None:
            node.cor = 0
            return
        if node.pai_.pai is None:
            return
        self.balancear_pos_insercao(node)

    def balancear_pos_insercao(self, node):
        while node.pai.cor == 1:
            if node.pai == node.pai.pai.direita:
                auxiliar = node.pai.pai.esquerda
                if auxiliar.cor == 1:
                    auxiliar.cor = 0
                    node.pai.cor = 0
                    node.pai.pai.cor = 1
                    node = node.pai.pai
                else:
                    if node == node.pai.esquerda:
                        node = node.pai
                        self.rotacao_direita(node)
                    node.pai.cor = 0
                    node.pai.pai.cor = 1
                    self.rotacao_esquerda(node.pai.pai)
            else:
                auxiliar = node.pai.pai.direita

                if auxiliar.cor == 1:
                    auxiliar.cor = 0
                    node.pai.cor = 0
                    node.pai.pai.cor = 1
                    node = node.pai.pai
                else:
                    if node == node.pai.direita:
                        node = node.pai
                        self.rotacao_esquerda(node)
                    node.pai.cor = 0
                    node.pai.pai.cor = 1
                    self.rotacao_direita(node.pai.pai)
            if node == self.raiz:
                break
        self.raiz.cor = 0

    def rotacao_esquerda(self, x):
        y = x.direita
        x.direita = y.esquerda
        if y.esquerda != self.TNULL:
            y.esquerda.pai = x
        y.pai = x.pai
        if x.pai is None:
            self.raiz = y
        elif x == x.pai.esquerda:
            x.pai.esquerda = y
        else:
            x.pai.direita = y
        y.esquerda = x
        x.pai = y
    
    def rotacao_direita(self, x):
        y = x.esquerda
        x.esquerda = y.direita
        if y.direita != self.TNULL:
            y.direita.pai = x
        y.pai = x.pai
        if x.pai is None:
            self.raiz = y
        elif x == x.pai.direita:
            x.pai.direita = y
        else:
            x.pai.esquerda = y
        y.direita = x
        x.pai = y
