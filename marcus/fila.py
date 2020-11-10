class Fila:

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.fila = []

    def inserir(self, elemento):
        if((self.tamanho) > len(self.fila)):
            return self.fila.append(elemento)
        print("Fila Cheia!")
    
    def remover(self):
        if(len(self.fila) > 0):
            elemento_removido = self.fila[0]
            del self.fila[0]
            return elemento_removido
        return False

    def mostrar_inicio(self):
        if(len(self.fila) > 0):
            return print(self.fila[0])
        return print("Fila Vazia!")

    def mostrar(self):
        if(len(self.fila) > 0):
            print(str(self.fila))
        elif(len(self.fila) == 0):
            print("Fila Vazia!")
        else: 
            print("Fila Cheia!")