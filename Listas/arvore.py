from nodeArvore import*

class Arvore:
    def __init__(self, dado):
        self.raiz = dado

    def mostrar_profundidade(self):
        visitados = set()
        visitados.add(self.raiz)
        falta_visitar = [self.raiz]
        resultado = ""
        while falta_visitar:
            vertice = falta_visitar.pop()
            resultado += str(vertice) + " | "
            for filho in vertice.proximo:
                if filho is not visitados:
                    visitados.add(filho)
                    falta_visitar.append(filho)
        print(resultado.rstrip("|"))
        
    def mostrar_largura(self):
        visitados = set()
        visitados.add(self.raiz)
        falta_visitar = [self.raiz] #   Falta visitar = Fila
        resultado = ""
        while falta_visitar:
            vertice = falta_visitar.pop()
            resultado += str(vertice) + " | "
            """ print("Teste Resultado: ", resultado) """
            for vizinho in vertice.proximo:
                """ print("Vertice.prox: ",vertice.proximo, "\nVizinho: ", vizinho, "\nFALTA VISITAR: ", falta_visitar,"\n") """
                if not vizinho in visitados:
                    falta_visitar.insert(0,vizinho)
            visitados.add(vertice)
        print(resultado.rstrip("|"))
            


