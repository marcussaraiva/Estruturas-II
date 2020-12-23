from node import *

class DequeDinamico:
    
    def __init__(self):
        self.tamanho = 0
        self.inicio = None
        self.fim = None
    
    def get_tamanho(self):
        return print(self.tamanho)

#----------PELA DIREITA----------#
    def inserir_final(self, dado):
        elemento = Node(dado)

        if(self.inicio is None) & (self.fim is None):
            self.fim = elemento
            self.inicio = elemento
            self.tamanho = 1
        else:
            elemento.anterior = self.fim
            self.fim.proximo = elemento
            self.fim = elemento
            elemento.proximo = None
            self.tamanho += 1

#----------PELA ESQUERDA----------#
    def inserir_inicio(self, dado):
        elemento = Node(dado)
        
        if(self.inicio is None) & (self.fim is None):
            self.fim = elemento
            self.inicio = elemento
            self.tamanho = 1
        else:
            elemento.proximo = self.inicio
            self.inicio.anterior = elemento
            self.inicio = elemento
            elemento.anterior = None
            self.tamanho += 1

#----------PELA DIREITA----------#
    def remover_final(self):
        if(((self.inicio is not None) & (self.inicio != self.fim)) & (self.fim is not None)):
            elemento = self.fim.anterior
            self.fim = elemento
            del self.fim.proximo
            self.fim.proximo = None
            self.tamanho -= 1
        else:
            del self.inicio
            del self.fim
            self.inicio = None
            self.fim = None
            self.tamanho -= 1
              
#----------PELA ESQUERDA----------#
    def remover_inicio(self):
        if(((self.inicio is not None) & (self.inicio != self.fim)) & (self.fim is not None)):
            elemento = self.inicio.proximo
            self.inicio = elemento
            del self.inicio.anterior
            self.inicio.anterior = None
            self.tamanho -= 1            
        else:
            del self.inicio
            del self.fim
            self.inicio = None
            self.fim = None
            self.tamanho -= 1

    def reinicializar(self):
        if(((self.inicio is not None) & (self.inicio != self.fim)) & (self.fim is not None)):
            while(self.inicio != self.fim):    
                elemento = self.inicio.proximo
                self.inicio = elemento
                del self.inicio.anterior
                self.inicio.anterior = None
                self.tamanho -= 1
            del self.inicio
            del self.fim
            self.inicio = None
            self.fim = None
            self.tamanho -= 1
        else:
            del self.inicio
            del self.fim
            self.inicio = None
            self.fim = None
            self.tamanho -= 1
        print("Reinicializado!")


    def mostrar(self):
        if((self.inicio is None) & (self.fim is None)):
            print("Deque Vazio!")
        else:
            elemento = self.inicio
            while(elemento != self.fim):
                print(str(elemento.dado))
                elemento = elemento.proximo

            print(str(elemento.dado))