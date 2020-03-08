class nodo:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.vecinos = set()

    def addVecino(self, vecinos):
        for vecino in vecinos:
            self.vecinos = self.vecinos.add(vecino)

class grafo:
    def __init__(self, n):
        self.nodos = set()
        self.nodos = self.nodos.add(nodo(0,0)) # el tablero vacío
        for i in range(1,n+1):
            for j in range(1, n+1):
                self.nodos = self.nodos.add(nodo(i, j))
        for v in self.nodos:
            enlazar(v, self.nodos)
