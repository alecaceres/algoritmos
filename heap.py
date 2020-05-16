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
        for v in self.nodes:
            v.d = float("inf")
            v.pi = None
        s.d = 0

class Node:
    def __init__(self, key):
        """
        Por defecto tiene las propiedades d = None (representando infinito) y
        pi = None (representando que no tiene un nodo padre). Además,
        inicialmente se considera que ese vértice no tiene vecinos.
        """
        self.key = key
        self.d = float("inf")
        self.pi = None
        self.neighbours = set()

    def addNeighbour(self, v, weight):
        '''
        Cada vecino de agrega de la forma (vecino, distancia)
        '''
        self.neighbours.add((v, weight))

class HeapVector:
    def __init__(self, queue: list):
        '''
        length representa el número de elementos que puede almacenar el vector.
        heap_size representa el número de elementos en el heap
        '''
        self.length = len(queue)
        self.heap_size = len(queue)
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
        if l <= self.heap_size and self.queue[l-1].d < self.queue[i-1].d: smallest = l
        else: smallest = i
        if r <= self.heap_size and self.queue[r-1].d < self.queue[smallest-1].d: smallest = r
        if smallest != i:
            self.queue[i-1], self.queue[smallest-1] = self.queue[smallest-1], self.queue[i-1]
            self.MinHeapify(smallest)

    def minimum(self):
        return self.queue[0]

    def ExtractMin(self):
        if not self.queue: raise ValueError("Heap Underflow")
        min = self.queue.pop(0)
        self.heap_size -= 1
        self.MinHeapify(1)
        return min

    def HeapDecreaseKey(self, i, key):
        '''
        Se encarga de actualizar la clave del nodo i con el nuevo valor key
        con key < A[i].
        '''
        self.queue[i] = key
        while i and self.queue[self.parent(i)].d > self.queue[i].d:
            self.queue[self.parent(i)], self.queue[i] = self.queue[i], self.queue[self.parent(i)]
            i = self.parent(i)

    def MinHeapInsert(self, key):
        self.heap_size += 1
        self.queue.append(float("inf"))
        self.HeapDecreaseKey(self.heap_size - 1, key)


def Relax(u, v, w):
    """
    u, v:   vértices
    w:      peso de la arista uv
    """
    if v.d > u.d + w:
        v.d = u.d + w
        v.pi = u

def yaml2graph(path = 'input_dijkstra.yaml'):
    import yaml
    '''
    El grafo se representa de la siguiente forma en el archivo yaml:
    key1: [[keyneighbour1, weight1], [keyneighbour2, weight2], ...]
    .
    .
    .
    keyN: [[keyneighbour1, weight1], ..., [keyneighbourN, weightN]]
    '''
    graph = yaml.load(open(path, 'r'), Loader=yaml.Loader)
    nodes = []
    for key, neighbours in graph.items():
        nodes.append(Node(key))
    for i, (key, neighbours) in enumerate(graph.items()):
        for neighbour in neighbours:
            try: neighbour_node = next(x for x in nodes if x.key == neighbour[0])
            except: print(f"No se encuentra nodo con la clave {key}.")
            nodes[i].addNeighbour(neighbour_node, neighbour[1])
    nodes.sort(key = lambda x: x.d)
    G = Graph(nodes)
    return G
