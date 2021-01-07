from quickSort import *
from mergeSort import *

class Deque:

        def __init__(self, tamanho):
            self.tamanho = tamanho
            self.inicio = None
            self.fim = None
            self.deque = []
        
        def get_tamanho(self):
            return print(len(self.deque))

#----------QUICKSORT----------#
        def quickSort(self):
            quickSort = QuickSort()
            quickSort.quicksort(self.deque)
            
#----------ORDENAR----------#
        def ordenar(self):
            for passagem in range(len(self.deque) - 1, 0, -1):     
                for i in range(passagem):
                    if(self.deque[i] > self.deque[i+1]):
                        troca = self.deque[i]
                        self.deque[i] = self.deque[i+1]
                        self.deque[i+1] = troca

#----------SELECTION-SORT----------#
        def selectionSort(self):
            for j in range(len(self.deque) - 1):
                indice_minimo = j
                for i in range (j, len(self.deque)):
                    if self.deque[i] < self.deque[indice_minimo]:
                        indice_minimo = i
                if self.deque[j] > self.deque[indice_minimo]:
                    auxiliar = self.deque[j]
                    self.deque[j] = self.deque[indice_minimo]
                    self.deque[indice_minimo] = auxiliar

#----------BUBBLE-SORT----------#
        def bubbleSort(self):
            for j in range(len(self.deque) -1 ):
                for i in range(len(self.deque) -1 ):
                    if self.deque[i] > self.deque[i+1]:
                        self.deque[i], self.deque[i+1] = self.deque[i+1], self.deque[i]

#----------MERGE-SORT----------#
        def mergeSort(self):        
            mergeSort = MergeSort()
            mergeSort.mergeSort(self.deque)

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
        