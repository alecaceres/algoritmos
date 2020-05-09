import yaml
import heap

def dijkstra(G, s):
    G.InitializeSingleSource(s)
    S = set()
    Q = heap.HeapVector(G.nodes)
    while Q.heap_size:
        u = Q.ExtractMin()
        S.add(u)
        for v in u.neighbours:
            v, w = v # v = vecino, w = peso
            heap.Relax(u, v, w)

def yaml2graph(path = 'input_dijkstra.yaml'):
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
        nodes.append(heap.Node(key))
    for i, (key, neighbours) in enumerate(graph.items()):
        for neighbour in neighbours:
            try: neighbour_node = next(x for x in nodes if x.key == neighbour[0])
            except: print(f"No se encuentra nodo con la clave {key}.")
            nodes[i].addNeighbour(neighbour_node, neighbour[1])
    nodes.sort(key = lambda x: x.key)
    G = heap.Graph(nodes)
    return G

G = yaml2graph()
for node in G.nodes: dijkstra(G, node)
