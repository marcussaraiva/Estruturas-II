from arvoreBinariaDeBusca import*
import random
def main():
    random.seed(77)
    dados = random.sample(range(1, 50), 42)
    bst = ArvoreBinariaBusca()
    for d in dados:
        bst.inserir(d)
    bst.mostrar_largura()

if __name__ == "__main__":
    main()