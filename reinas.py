class nodo:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.vecinos = []

    def addVecino(self, vecinos):
        for vecino in vecinos:
            self.vecinos.append(vecino)

class grafo:
    def __init__(self, n):
        self.nodos = []
        self.nodos.append(nodo(0,0)) # el tablero vacío
        for i in range(1,n+1):
            for j in range(1, n+1):
                self.nodos.append(nodo(i, j))
