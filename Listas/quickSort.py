class QuickSort:

    def partition(self, deque, inicio, fim):
        pivo = deque[fim]
        i = inicio
        for j in range(inicio, fim):
            if deque[j] <= pivo:
                deque[j], deque[i] = deque[i], deque[j]
                i = i + 1
        deque[i], deque[fim] = deque[fim], deque[i]
        return i
    
    def quicksort(self, deque, inicio=0, fim=None):
        if fim is None:
            fim = len(deque)-1
        if inicio < fim:
            pivot = self.partition(deque, inicio, fim)
            self.quicksort(deque, inicio, pivot-1)
            self.quicksort(deque, pivot+1, fim)
    
    
    

