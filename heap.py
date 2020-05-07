class Graph:
    def __init__(self, nodes):
        """
        Atributo: nodes. Es una lista de los nodos de ese grafo.
        """
        self.nodes = nodes

    def InitializeSingleSource(self, s):
        """
        Se asigna s.d = 0, ya que la distancia de la fuente a si misma es cero
        """
        s.d = 0

class Node:
    def __init__(self):
        """
        Por defecto tiene las propiedades d = None (representando infinito) y
        pi = None (representando que no tiene un nodo padre). Además,
        inicialmente se considera que ese vértice no tiene vecinos.
        """
        self.d = None
        self.pi = None
        self.neighbours = set()

    def addNeighbour(self, v, weight):
        '''
        Cada vecino de agrega de la forma (vecino, distancia)
        '''
        self.neighbours.add((v, weight))

    def getDistance(self, v):
        '''
        Cálculo del peso de la arista self-v
        '''
        for neighbour in self.neighbours:
            if v is neighbour[0]:
                return neighbour[1]

class HeapVector:
    def __init__(self, queue: list):
        '''
        length representa el número de elementos que puede almacenar el vector.
        heap_size representa el número de elementos en el heap
        '''
        self.length = len(queue)
        self.heap_size = 0
        self.queue = queue

    def parent(self, i):
        '''
        Función para acceder al padre de i
        '''
        return i//2

    def left(self, i):
        '''
        Función para acceder al hijo izquierdo de i
        '''
        return 2*i

    def right(self, i):
        '''
        Función para acceder al hijo derecho de i
        '''
        return 2*i+1

    def MinHeapify(self,i):
        '''
        Mantiene la propiedad del heap intercambiando los valores de
        los nodos del ́arbol

        A: objeto de la clase HeapVector
        '''
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size and self.queue[l] < self.queue[i]: smallest = l
        else: smallest = i
        if r <= self.heap_size and self.queue[r] < self.queue[smallest]: smallest = r
        if smallest != i:
            self.queue[i], self.queue[smallest] = self.queue[smallest], self.queue[i]
            self.MinHeapify(smallest)

    def minimum(self):
        return self.queue[0]

    def ExtractMin(self):
        try: min = self.queue.pop(0)
        except: print("ERROR. Heap underflow."); sys(-1)
        self.heap_size -= 1
        self.MinHeapify(0)
        return min

    def HeapDecreaseKey(self, i, key):
        '''
        Se encarga de actualizar la clave del nodo i con el nuevo valor key
        con key < A[i].
        '''
        self.queue[i] = key
        while i>1 and self.queue[self.parent(i)] > self.queue[i]:
            self.queue[self.parent(i)], self.queue[i] = self.queue[i], self.queue[self.parent(i)]
            i = self.parent(i)

    def MinHeapInsert(self, key):
        self.heap_size += 1
        self.queue[self.heap_size] = None
        self.HeapDecreaseKey(self.heap_size, key)


def Relax(u, v, w):
    """
    u, v:   vértices
    w:      peso de la arista uv
    """
    if v.d > u.d + w:
        v.d = u.d + w
        v.pi = u
