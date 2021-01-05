from NodeArvoreAVL import *

class ArvoreAVL(object):
    def inserir(self, raiz, chave):
         if not raiz:
            return NodeArvoreAVL(chave)
        elif chave < raiz.valor:
            raiz.esquerda = self.inserir(raiz.esquerda, chave)
        else:
            raiz.direta = self.inserir(raiz.direita, chave)
        raiz.altura = 1 + max(self.getAltura(raiz.esquerda), self.getAltura(raiz.direita))
        balanco = self.getBalanceamento(raiz)
        if balanco > 1 and chave < raiz.esquerda.valor:
            return self.rotacao_esquerda(raiz)
        if balanco < -1 and chave > raiz.direita.valor:
            return self.rotacao_direita(raiz)
        if balanco > 1 and chave > raiz.esquerda.valor:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)
        if balanco < -1 and chave < raiz.direita.valor:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)
        return raiz
    
    def getAltura(self, raiz):
        if not raiz:
            return 0
        return raiz.altura

    def getBalanceamento(self, raiz):
        if not raiz:
            return 0
        return self.getAltura(raiz.esquerda) - self.getAltura(raiz.direita)

    def rotacao_esquerda(self, x):
        y = x.esquerda
        T3 = y.direita
        y.esquerda = x
        x.direita = T3
        x.altura = 1 + max(self.getAltura(x.esquerda), self.getAltura(x.direita))
        y.altura = 1 + max(self.getAltura(y.esquerda), self.getAltura(y.direita))
        return y

    def rotacao_direita(self, x):
        y = x.direita
        T2 = y.esquerda
        y.esquerda = x
        x.direita = T2
        x.altura = 1 + max(self.getAltura(x.esquerda), self.getAltura(x.direita))
        y.altura = 1 + max(self.getAltura(y.esquerda), self.getAltura(y.direita))
        return y