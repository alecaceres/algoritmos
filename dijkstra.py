import yaml
import heap

def dijkstra(G, w, s):
    '''
    '''
    G.InitializeSingleSource(s)
    S = set()
    # Q = G.V
    while Q:
        u = Q.ExtractMin()
        S.add(u)
        #for v in G.Adj[u]:
        w = u.getDistance(v)
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
        node = heap.Node()
        for neighbour in neighbours:
            node.addNeighbour(neighbour[0], neighbour[1])
        nodes.append(node)
    G = heap.Graph(nodes)
    return G

G = yaml2graph()
