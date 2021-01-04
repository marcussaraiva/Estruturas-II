class NodeArvoreBinaria:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return str(self.dado)