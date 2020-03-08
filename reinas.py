class nodo:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.vecinos = set()

    def addVecino(self, vecinos):
        for vecino in vecinos:
            self.vecinos.add(vecino)

class grafo:
    def __init__(self, n):
        self.filas = set()
        self.filas.add(tuple([nodo(0,0)])) # el tablero vacío
        for i in range(1,n+1):
            fila = []
            for j in range(1, n+1):
                fila.append(nodo(i, j))
            self.filas.add(tuple(fila))
        self.recorrerFilas(n)

    def recorrerFilas(tablero, n):
        for fila in tablero.filas:
            if fila[0].fila != n:
                filaVecino = fila[0].fila + 1
                for fila2 in tablero.filas:
                    if fila2[0].fila == filaVecino:
                        vecinos = set()
                        for v in fila2:
                            vecinos.add(v)
                for v in fila:
                    v.addVecino(vecinos)

a = grafo(8)
