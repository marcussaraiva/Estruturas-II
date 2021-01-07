class MergeSort:
    def mergeSort(self, deque, inicio=0, fim=None):        
            if fim is None:
                fim = len(deque)
            if (fim - inicio > 1):
                meio = (fim + inicio) // 2
                self.mergeSort(deque, inicio, meio)
                self.mergeSort(deque, meio, fim)
                self.merge(deque, inicio,meio, fim)
        
    def merge(self, deque, inicio, meio, fim):
            esquerda = deque[inicio:meio]
            direita = deque[meio:fim]
            topo_esquerda, topo_direita = 0, 0
            for k in range(inicio, fim):
                if topo_esquerda >= len(esquerda):
                    deque[k] = direita[topo_direita]
                    topo_direita = topo_direita + 1
                elif topo_direita >= len(direita):
                    deque[k] = esquerda[topo_esquerda]
                    topo_esquerda = topo_esquerda + 1
                elif esquerda[topo_esquerda] < direita[topo_direita]:
                    deque[k] = esquerda[topo_esquerda]
                    topo_esquerda = topo_esquerda + 1
                else:
                    deque[k] = direita[topo_direita]
                    topo_direita = topo_direita + 1