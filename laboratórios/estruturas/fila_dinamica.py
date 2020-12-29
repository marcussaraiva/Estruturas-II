#
# Utilizaremos a classe Fila para definir as principais funções 
# da estrutura linear mais trivial - fila estática. Em seguida, 
# estenderemos a classe para suportar uma fila dinâmica.
#
class FilaDinamica:
    
    def __init__(self):
        self.fim = None
        self.inicio = None
        self.tamanho = 0

    def get_tamanho(self):
        return self.tamanho
    
    # Em uma fila, a inserção é feita ao fim da lista.
    # Por se tratar de uma estrutura estática, há uma
    # restrição de tamanho da lista que precisa ser 
    # avaliada antes de permitir a inserção
    def insere(self, elemento):
        elem = Node(elemento)
        
        # Quando a fila está vazia
        if ((self.inicio is None) and (self.fim is None)):
            self.inicio = elem
            self.fim = elem
        else:
            # O novo elemento deve apontar para quem estava 
            # no fim apontar para o novo elemento
            elem.prox = self.fim
            self.fim = elem
        self.tamanho += 1
        return self.inicio

    # Em uma fila, a remoção é feita do primeiro elemento
    # da lista (o primeiro a entrar, é o primeiro a sair)
    def remove(self):
        elem = self.fim
        if (self.inicio is None):
            return None
        
        elem_removido = self.inicio
        
        while (elem.prox != elem_removido):
            elem = elem.prox
        
        elem.prox = None
        self.inicio = elem
        self.tamanho -= 1
        return elem_removido
        
    def vazia(self):
        return (self.inicio is None)
    
    def peek(self):
        return self.inicio.conteudo
    
    def mostra(self):
        pont = self.fim
        if(pont is None):
            print("Lista vazia")
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