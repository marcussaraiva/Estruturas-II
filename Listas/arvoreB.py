from NodeArvoreB import *

class ArvoreB:
    def __init__(self, d):
        self.raiz = NodeArvoreB(True)
        self.d = d

    def inserir(self, chave):
        raiz = self.raiz
        if len(raiz.chaves) == (2 * self.d) - 1:
            temp = NodeArvoreB()
            self.raiz = temp
            temp.filho.inserir(0, raiz) 
            self.separar(temp, 0)
            self.inserir_nao_cheia(temp, chave)
        else:
            self.inserir_nao_cheia(raiz, chave)

    def inserir_nao_cheia(self, arvore, chave):
        i = len(arvore.chaves) - 1
        if arvore.folha:
            arvore.chaves.append((None, None))
            while i >= 0 and chave[0] < arvore.chaves[i][0]:
                arvore.chaves[i + 1] = arvore.chaves[i]
                i -= 1
            arvore.chaves[i + 1] = chave
        else:
            while i >= 0 and chave[0] < arvore.chaves[i][0]:
                i -= 1
            i += 1
            if len(arvore.filho[i].chaves) == (2 * self.d) - 1:
                self.separar(arvore, i)
                if chave[0] > arvore.chaves[i][0]:
                    i += 1
            self.inserir_nao_cheia(arvore.filho[i], chave)
     
     def separar(self, arvore, i):
        d = self.d
        y = arvore.filho[i]
        z = NodeArvoreB(y.folha)
        arvore.filho.inserir(i + 1, z)
        arvore.chaves.inserir(i, y.chaves[d - 1])
        z.chaves = y.chaves[d: (2 * d) - 1]
        y.chaves = y.chaves[0: d - 1]
        if not y.folha:
            z.filho = y.filho[d: 2 * d]
            y.filho = y.filho[0: d]
    
    def busca(self, chave, node=None):
        if node is not None:
            i = 0
            while i < len(node.chaves) and chave > node.chaves[i][0]:
                i += 1
            if i < len(node.chaves) and chave == node.chaves[i][0]:
                return node, i
            elif node.folha:
                return None
            else:
                return self.busca(chave, node.filho[i])
        else:
            return self.busca(chave, self.raiz)
