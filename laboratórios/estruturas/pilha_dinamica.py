#
# Utilizaremos a classe Fila para definir as principais funções 
# da estrutura linear mais trivial - fila estática. Em seguida, 
# estenderemos a classe para suportar uma fila dinâmica.
#
class PilhaDinamica:
    
    def __init__(self):
        self.topo = None
        self.inicio = None
        self.tamanho = 0

    def get_tamanho(self):
        return self.tamanho
    
    # Há um nome consolidado na literatura para inserções
    # em pilhas - push. Segui este padrão para implementar
    # inserções em pilhas
    def push(self, elemento):
        elem = Node(elemento)
        
        # Quando a pilha está vazia
        if ((self.inicio is None) and (self.topo is None)):
            self.inicio = elem
            self.topo = elem
        else:
            # O elemento pilha que está no topo passa a 
            # apontar para o novo elemento
            self.topo.prox = elem
            self.topo = elem
        self.tamanho += 1
        return self.topo

    # Há um nome consolidado na literatura para remoções
    # em pilhas - pop. Segui este padrão para implementar
    # inserções em pilhas
    # no caso da pilha dinâmica, só temos ponteiro para o 
    # próximo elemento. Para pegar o penúltimo elemento, 
    # tive que percorrer toda a pilha (a partir do início)
    def pop(self):
        proximo_no = self.inicio
        while (proximo_no.prox != self.topo):
            proximo_no = proximo_no.prox
        
        proximo_no.prox = None
        self.topo = proximo_no
        
        if (self.inicio is None):
            return None
        
        self.tamanho -= 1
        return proximo_no
        
    def vazia(self):
        return (self.inicio is None)
    
    def peek(self):
        return self.topo.conteudo
    
    def mostra(self):
        pont = self.inicio
        if(pont is None):
            print("Pilha vazia")
        lista_str = ""
        while (pont is not None):
            lista_str += str(pont.conteudo) + ' >> '
            pont = pont.prox

        print( lista_str.rstrip(' >> '))



# Criei uma classe para estruturar o nó das listas
# nela, guardamos o ponteiro para o próximo elemento
# e o seu conteúdo
class Node:
    def __init__(self, conteudo):
        self.prox = None
        self.conteudo = conteudo