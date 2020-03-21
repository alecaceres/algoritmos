import numpy

import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)


class nodo:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.vecinos = []

    def __str__(self):
        print("Posicion:", self.fila, ",", self.columna, "\nVecinos:")
        for vecino in self.vecinos:
            print("(", vecino.fila, ",", vecino.columna, ")")
        return "\n"

class grafo:
    def __str__(self):
        for posicion in self.nodos:
            print(posicion)
        return "\n"

    def __init__(self, n):
        self.nodos = set()
        for i in range(1,n+1):
            for j in range(1, n+1):
                self.nodos.add(self.addNodos(n, nodo(i,j)))

    def addNodos(self, dim, celda = nodo(1,1)):
        i = celda.fila
        j = celda.columna
        centro = (dim + 1)/2
        vecinos = {tuple([i-1, j-2]), tuple([i-1, j+2]), tuple([i+1, j-2]), tuple([i+1, j+2]),
                tuple([i-2, j-1]), tuple([i-2, j+1]), tuple([i+2, j-1]), tuple([i+2, j+1])}
        vecinos = limpiar(vecinos, dim) # eliminar las celdas inválidas
        for ordenar in range(dim-1, -1, -1): # para priorizar aquellos que estén en los costados
          for i,j in vecinos:
            if abs(i - centro) + abs(j - centro) == ordenar:
              celda.vecinos.append(nodo(i,j))
        return celda

def limpiar(lista, dim):
    lista2 = lista.copy()
    for elemento in lista:
        if noesValido(elemento, dim):
            lista2.remove(elemento)
    return lista2

def noesValido(tupla, dim):
    i, j = tupla
    return i<1 or j<1 or i>dim or j>dim

def matprint(mat, fmt="g"):
    col_maxes = [max([len(("{:"+fmt+"}").format(x)) for x in col]) for col in mat.T]
    for x in mat:
        for i, y in enumerate(x):
            print(("{:"+str(col_maxes[i])+fmt+"}").format(y), end="  ")
        print("")

def knightTour(nodos, caballo, N, mat, num = 1):
    row = caballo.fila
    col = caballo.columna
    if mat[row-1,col-1]:
        return False
    mat[row-1,col-1] = num
    if num == N**2:
        matprint(mat)
        return True
    for vecino in caballo.vecinos:
        vecino = next((x for x in nodos if x.fila == vecino.fila and x.columna == vecino.columna), None)
        if knightTour(nodos, vecino, N, mat, num + 1):
            return True
    mat[row-1,col-1] = 0
    return False

def solucion(N, row, col):
    if N%2 == 1 or N < 6: return "No Circuit Tour.\n"
    tablero = grafo(N)
    caballo = next((x for x in tablero.nodos if x.fila == row and x.columna == col), None)
    mat = numpy.zeros((N,N), dtype = numpy.uint16)
    if knightTour(tablero.nodos, caballo, N, mat): return ""

for line in sys.stdin:
    linea = line.rstrip() # se eliminan los saltos de línea de creados al leer las líneas de sys.stdin
    N, row, col = [int(x) for x in linea.split()]
    print(solucion(N, row, col))
