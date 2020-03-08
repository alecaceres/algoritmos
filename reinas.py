class nodo:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.vecinos = []

class grafo:
    def __init__(self, n):
        nodo(0,0) # el tablero vacío
        for i in range(1,n+1):
            for j in range(1, n+1):
                nodo(i, j)
