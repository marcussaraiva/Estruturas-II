class Node:

    def __init__(self, dado):
        self.dado = dado
        self.proximo = []

    def inserir(self, dado):
        self.proximo.insert(0, dado)

    def __str__(self):
        return str(self.dado)
