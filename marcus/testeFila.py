from fila import *

def main():
    fila = Fila(5)
    fila.inserir("Joao1")
    fila.mostrar_inicio()
    fila.mostrar()
    fila.remover()

if __name__ == "__main__":
    main()