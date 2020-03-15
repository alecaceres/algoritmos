import numpy
import time
class nodo:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.vecinos = set()

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

    def __init__(self, n = 8):
        self.nodos = set()
        for i in range(1,n+1):
            for j in range(1, n+1):
                self.nodos.add(self.addNodos(n, nodo(i,j)))

    def addNodos(self, dim = 8, celda = nodo(1,1)):
        i = celda.fila
        j = celda.columna
        vecinos = {tuple([i-1, j-2]), tuple([i-1, j+2]), tuple([i+1, j-2]), tuple([i+1, j+2]),
                tuple([i-2, j-1]), tuple([i-2, j+1]), tuple([i+2, j-1]), tuple([i+2, j+1])}
        vecinos = limpiar(vecinos, dim) # eliminar las celdas inválidas
        for i,j in vecinos:
            celda.vecinos.add(nodo(i,j))
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

def knightTour(tablero, caballo, N, mat, num = 1):
    row = caballo.fila
    col = caballo.columna
    if num == N**2 and mat[row-1,col-1] == 1 and mat.all():
        print(mat, "\n")
        return True
    if mat[row-1,col-1]:
        return False
    mat[row-1,col-1] = num
    for vecino in caballo.vecinos:
        vecino = next((x for x in tablero.nodos if x.fila == vecino.fila and x.columna == vecino.columna), None)
        if knightTour(tablero, vecino, N, mat, num + 1):
            return True
    mat[row-1,col-1] = 0
    return False

def haySolucion(tablero,  N = 8):
    mat = numpy.zeros((N,N), dtype=numpy.int8)
    if N%2:
        centro = (N+1)//2
        for i in range(N):
            for caballo in tablero.nodos:
                if abs(caballo.fila - centro) + abs(caballo.columna - centro) == i:
                    print(caballo)
                    if knightTour(tablero, caballo, N, mat):
                        return True
    centro = (N+1)/2
    for i in range(N):
        for caballo in tablero.nodos:
            if abs(caballo.fila - centro) + abs(caballo.columna - centro) == i:
                print(caballo)
                if knightTour(tablero, caballo, N, mat):
                    return True
    return False

def teoria(N):
    if N%2 == 1 or N < 5: return "No Circuit Tour."
    return "Bueno"

start = time.time()
n = 6
a = grafo(n)
print("Creado en", time.time() - start)
#print(haySolucion(a,n))
print(teoria(n))
print("Se tardo", time.time() - start)
