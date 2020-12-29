#
# Utilizaremos a classe Fila para definir as principais funções 
# da estrutura linear mais trivial - fila estática. Em seguida, 
# estenderemos a classe para suportar uma fila dinâmica.
#
class Fila:
    
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.inicio = -1
        self.elementos = []

    # Em uma fila, a inserção é feita ao fim da lista.
    # Por se tratar de uma estrutura estática, há uma
    # restrição de tamanho da lista que precisa ser 
    # avaliada antes de permitir a inserção    
    def insere(self, elemento):
        if((self.tamanho) > len(self.elementos)):
            return self.elementos.append(elemento)
        print("Estouro de fila")
    
    # Em uma fila, a remoção é feita do primeiro 
    # elemento da lista (o primeiro a entrar, é o 
    # primeiro a sair)
    def remove(self):
        if (len(self.elementos) > 0):
            elemento = self.elementos[0]
            del self.elementos[0]
            return elemento
        return false
    
    # Para permitir o usuário acompanhar o tamanho da
    # fila, defini um método de apoio get_tamanho
    def get_tamanho(self):
        return len(self.elementos)
    
    def vazia(self):
        return (len(self.elementos) == 0)
    
    def peek(self):
        return self.elementos[0]
    
    def mostra(self):
        if(len(self.elementos)!=0):
            print(str(self.elementos))
        else:
            print("Fila vazia")