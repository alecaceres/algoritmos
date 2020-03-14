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
    def __str__(self):
        for posicion in self.nodos:
            print(posicion)
        return "\n"

    def agregar(celdas, i, j):
        for celda in celdas.nodos:
            if celda.fila == i and celda.columna == j: #si la celda que se quiere agregar ya está en el set
                return celdas

        celda = nodo(i,j)
        celda.addVecino(celdas.nodos)
        celdas.nodos.add(celda)

    def __init__(self, n = 8):
        self.nodos = set()
        self.soluciones = 0

        self.addNodos(n)

        for node in self.addNodos(n):
            self.nodos.add(node)
            if len(self.nodos) == n**2: break
        #for i in range(1,n+1):
        #    for j in range(1, n+1):
        #        self.agregar(i, j)
        #        self.nodos.add(nodo(i, j))
                #y tiene que agregar tambien los vecinos, y esos vecinos su vecinos y así ir verificando también que no se agregen lo mismo
                #dos veces. Siempre que se cree un vecino, asignar también como vecino al nodo anterior

    def addNodos(self, dim = 8, celda = nodo(1,1)):
        i = celda.fila
        j = celda.columna
        print(i, j)
        vecinos = {tuple([i-1, j-2]), tuple([i-1, j+2]), tuple([i+1, j-2]), tuple([i+1, j+2]),
                tuple([i-2, j-1]), tuple([i-2, j+1]), tuple([i+2, j-1]), tuple([i+2, j+1])}
        vecinos = limpiar(vecinos, dim) # eliminar las celdas inválidas
        print(vecinos)
        for i,j in vecinos:
            existe = False
            for nodito in self.nodos:
                if nodito.fila == i and nodito.columna == j:
                    existe = True
                    break
            if not existe:
                nodito = nodo(i,j)
            nodito.vecinos.add(celda)
            celda.vecinos.add(nodito)
        #self.nodos.add(celda)
        for vecino in celda.vecinos:
            yield self.addNodos(dim, vecino)
            print("Tamaño:",len(self.nodos),"\n")
        yield celda

def limpiar(lista, dim):
    lista2 = lista.copy()
    for elemento in lista:
        if noesValido(elemento, dim):
            lista2.remove(elemento)
    return lista2

def noesValido(tupla, dim):
    i, j = tupla
    return i<1 or j<1 or i>dim or j>dim

a = grafo(3)
print(a)
print(len(a.nodos))
