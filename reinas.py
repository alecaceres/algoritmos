class nodo:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.vecinos = set()

    def addVecino(self, vecinos):
        for vecino in vecinos:
            self.vecinos.add(vecino)

    def __str__(self):
        print("Posicion:", self.fila, ",", self.columna, "\nVecinos:")
        for vecino in self.vecinos:
            print("(", vecino.fila, ",", vecino.columna, ")")
        return "\n"

class grafo:
    def __init__(self, n = 8):
        self.filas = set()
        self.soluciones = 0
        self.raiz = nodo(0,0)

        self.filas.add(tuple([self.raiz])) # el tablero vacío
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

    def __str__(self): # sirve para saber si los nodos fueron correctamente enlazados.
        for fila in self.filas:
            for v in fila:
                print(v)
        return ""

def solucion(tablero):
    colocarReina(tablero, [], tablero.raiz)
    return tablero.soluciones

def colocarReina(tablero, reinas, reina): # la entrada son las reinas colocadas y la nueva reina
    #print("=============================================\n", reina)
    if reina.fila != 0:
        reinas.pop()

    for r in reinas:
        if abs(r.fila - reina.fila) == abs(r.columna - reina.columna) or r.columna == reina.columna:
            #print(r)
            return

    if len(reina.vecinos) == 0:
        tablero.soluciones = tablero.soluciones + 1
        return

    for vecino in reina.vecinos:
        reinas2 = reinas
        reinas2.append(vecino)
        colocarReina(tablero, reinas2, vecino)

a = grafo() # por defecto es de 8x8
print("El problema tiene", solucion(a), "soluciones")
