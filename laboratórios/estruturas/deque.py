#
# Utilizaremos a classe Deque para definir as principais funções 
# da estrutura linear mais trivial - estática. Em seguida, esten
# deremos a classe para suportar um deque dinamico.
#
class Deque:
    
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.inicio_esquerda = -1
        self.inicio_direita = tamanho
        self.elementos = []
    
    def get_tamanho(self):
        return len(self.elementos)
    
    # Há um nome consolidado na literatura para inserções
    # em pilhas - push. Segui este padrão para implementar
    # inserções em pilhas
    def insere_esq(self, elemento):
        if(self.tamanho == len(self.elementos)):
            print("Deque cheio")
        else:
            return self.elementos.insert(0,elemento)
        

    def insere_dir(self, elemento):
        if(self.tamanho == len(self.elementos)):
            print("Deque cheio")
        else:
            return self.elementos.append(elemento)
            self
            
    # 
    def remove_dir(self):
        if (len(self.elementos) > 0):
            return self.elementos.pop()
        return false

    # 
    def remove_esq(self):
        if (len(self.elementos) > 0):
            elemento_removido = self.elementos[0]
            del self.elementos[0]
            return elemento_removido
        return false

    # Retorna Verdadeiro se a lista estiver vazia
    def vazia(self):
        return (len(self.elementos) == 0)
    
    # Exibe os elementos do Deque
    def mostra(self):
        if(len(self.elementos)!=0):
            print(str(self.elementos))
        else:
            print("Deque vazio")