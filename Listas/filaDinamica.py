from node import *

class FilaDinamica:
    
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def inserir(self, dado):
        elemento = Node(dado)

        if((self.inicio is None) & (self.fim is None)):
            self.inicio = elemento
            self.fim = elemento
        else:
            elemento.proximo = self.fim
            self.fim = elemento.dado
        
        self.tamanho += 1
        return self.inicio

    def mostrar(self):
        ponteiro = self.fim

        if(ponteiro is None):
            print("Lista Vazia!")
        lista = ""
        while(ponteiro is not None):
            lista += str(ponteiro.dado) 
            ponteiro = ponteiro.proximo

        print(lista)
