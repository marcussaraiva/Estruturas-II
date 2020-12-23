class Deque:

        def __init__(self, tamanho):
            self.tamanho = tamanho
            self.inicio = None
            self.fim = None
            self.deque = []
        
        def get_tamanho(self):
            return print(len(self.deque))

        def inserir_inicio(self,elemento):
            if(self.tamanho == len(self.deque)):
                print("Deque cheio")
            else: return self.deque.insert(0,elemento)

        def inserir_final(self,elemento):
            if(self.tamanho == len(self.deque)):
                print("Deque cheio")
            else: return self.deque.append(elemento)

        def remover_inicio(self):
            if(len(self.deque) > 0):
                elemento_removido = self.deque[0]
                del self.deque[0]
                return elemento_removido
            return False
 
        def remover_final(self):
            if(len(self.deque) > 0):
                return self.deque.pop()
            return False
#
#                  REMOÇÃO POR ÍNDICE
#
        def remover_por_indice(self, indice):
            if(len(self.deque) > 0):
                elemento_removido = self.deque[indice]
                del self.deque[indice]
                return elemento_removido
            return False

        def mostrar(self):
            if(len(self.deque) > 0):
                print(str(self.deque))
            elif(len(self.deque) == 0):
                print("Fila Vazia!")
        