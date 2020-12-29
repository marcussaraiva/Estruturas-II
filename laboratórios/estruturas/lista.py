#
# Utilizaremos a classe Lista para definir as principais funções 
# da estrutura linear sem restrições.
#
class Lista:
    
    def __init__(self):
        self.inicio = None

    def insere(self, elemento, posicao):
        return False
        
    def insere_esq(self, elemento):
        node = Node(elemento)
        if(self.inicio is None):
            self.inicio = node
        else:
            node.proximo = self.inicio
            self.inicio = node
        return node
        
    def insere_dir(self, elemento):
        node = Node(elemento)
        if(self.inicio is None):
            self.inicio = node
        else:
            ult_node = self.inicio
            # procurar o ultimo no da lista
            while (ult_node.proximo is not None):
                ult_node = ult_node.proximo
            ult_node.proximo = node
        return node
    
    def remove_esq(self):
        node = self.inicio
        if (node is not None):
            self.inicio = node.proximo
            del node
            return self.inicio
        return False
    
    def remove_dir(self):
        node_anterior = self.inicio
        if (node_anterior.proximo is None):
            self.inicio = None
            del node_anterior
        else:
            node = self.inicio.proximo
        # percorrer toda lista
        while(node.proximo is not None):
            node_anterior = node
            node = node.proximo
        del node
        node_anterior.proximo = None
        return self.inicio
    
    def remove(self, elemento, posicao):
        #implemente o remove na posicao
        return False
        
    def ordena(self):
        #implemente a ordenação da lista
        return False
    
    def pesquisa(self, elemento):
        node = self.inicio
        while (node is not None):
            chave = str(node.conteudo)
            if (chave == str(elemento)):
                return node
            node = node.proximo
        return "Elemento não encontrado"
    
    # Para permitir o usuário acompanhar o tamanho da
    # lista, defini um método de apoio get_tamanho
    def get_tamanho(self):
        node = self.inicio
        tamanho = 0
        while(node is not None):
            tamanho += 1
            node = node.proximo
        return tamanho
    
    def vazia(self):
        return (self.inicio is None)
        
    def mostra(self):
        if(self.inicio is None):
            print("Lista vazia")
        else:
            node = self.inicio
            lista_str = ""
            while (node is not None):
                lista_str += str(node.conteudo) + " >> "
                node = node.proximo
            print(lista_str.rstrip(' >> '))

class Node:
    def __init__(self, valor):
        self.proximo = None
        self.conteudo = valor
        
    def __str__(self):
        return str(self.conteudo)