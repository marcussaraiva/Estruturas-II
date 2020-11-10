class Pilha:
    
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.topo = -1
        self.elementos = []
    
    def inserir(self,elemento):
        if((self.tamanho-1) > self.topo):
            self.topo += 1
            return self.elementos.append(elemento)
        print("Pilha Cheia!")    
    
    def remover(self):
        if(len(self.elementos) > 0):
            self.topo -= 1
            return self.elementos.pop()
        return False
    
    def mostrar_topo(self):
        if(len(self.elementos) > 0):
            return print(self.elementos[self.topo])
        return print("Pilha Vazia!")

    def mostrar(self):
        if(len(self.elementos) != 0):
            print(str(self.elementos))
        elif(len(self.elementos) == 0):   
            print("Pilha Vazia!")
        else:
            print("Pilha Cheia!")
