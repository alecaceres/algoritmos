import sys

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
        self.raiz = nodo(0,0)
        self.soluciones = 0
        self.list_soluciones = []

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

def solucion(tablero, row, col):
    colocarReina(tablero, [], tablero.raiz, row, col)



def colocarReina(tablero, reinas, reina, row, col): # la entrada son las reinas colocadas y la nueva reina
    if reina.fila == row and reina.columna != col:
        return
    sol = ""
    for r in reinas:
        if abs(r.fila - reina.fila) == abs(r.columna - reina.columna) or r.columna == reina.columna:
            return
        sol = sol + str(r.columna) + " "
    if len(reina.vecinos) == 0:
        sol = sol + str(reina.columna)
        tablero.soluciones += 1
        print(" " + str(tablero.soluciones) + "\t" + sol)
        tablero.list_soluciones.append(sol)
        return

    if reina.fila: reinas.append(reina)

    for vecino in reina.vecinos:
        colocarReina(tablero, reinas.copy(), vecino, row, col)

for line in sys.stdin:
    linea = line.rstrip() # se eliminan los saltos de línea de creados al leer las líneas de sys.stdin
    if len(linea) > 1:
        print("SOLN       ROW\n #      1 2 3 4 5 6 7 8\n")
        row, col = [int(x) for x in linea.split()]
        solucion(grafo(), col, row)
        print("\n")
