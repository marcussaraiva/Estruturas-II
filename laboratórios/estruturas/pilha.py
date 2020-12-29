#
# Utilizaremos a classe Pilha para definir as principais funções 
# da estrutura linear mais trivial - estática. Em seguida, esten
# deremos a classe para suportar uma pilha dinamica.
#
class Pilha:
    
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.topo = -1
        self.elementos = []
    
    def get_tamanho(self):
        return len(self.elementos)
    
    # Há um nome consolidado na literatura para inserções
    # em pilhas - push. Segui este padrão para implementar
    # inserções em pilhas
    def push(self, elemento):
        if((self.tamanho-1) > self.topo):
            self.topo += 1
            return self.elementos.append(elemento)
        print("Estouro de pilha")

    # Há um nome consolidado na literatura para remoções
    # em pilhas - pop. Segui este padrão para implementar
    # inserções em pilhas
    def pop(self):
        if (len(self.elementos) > 0):
            self.topo -= 1
            return self.elementos.pop()
        return false
        
    def vazia(self):
        return (len(self.elementos) == 0)
    
    def peek(self):
        return self.elementos[self.topo]
    
    def mostra(self):
        if(len(self.elementos)!=0):
            print(str(self.elementos))
        else:
            print("Pilha vazia")