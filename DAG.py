import heap

def TopologicalSort(G):
    from collections import deque
    '''
    llamar a DFS(G) para computar los tiempos v.f de cada vertice v
    cada vez que se termina de visitar un vertice, agregarlo al frente de una lista enlazada
    '''

    order, enter, state = deque(), set(G.nodes), {}
    GREY, BLACK = 0, 1
    def dfs(node):
        state[node] = GREY
        for k, w in node.neighbours:
            sk = state.get(k, None)
            if sk == GREY: raise ValueError("El gráfico contiene ciclos")
            if sk == BLACK: continue
            enter.discard(k)
            dfs(k)
        order.appendleft(node)
        state[node] = BLACK

    while enter: dfs(enter.pop())
    return order

def DAGShortestPaths(G, s):
    order = TopologicalSort(G)
    G.InitializeSingleSource(s)
    for u in order:
        for (v, w) in u.neighbours:
            heap.Relax(u,v,w)

G = heap.yaml2graph(path = 'input_DAG.yaml')
for node in G.nodes:
    graph = G
    DAGShortestPaths(G, node)
    for x in G.nodes:
        if x != node:
            try: print(f"Distancia de {node.key} a {x.key}\t: {x.d}.\t\tPadre de {x.key}: {x.pi.key}")
            except: print(f"Distancia de {node.key} a {x.key}\t: {x.d}.\t\tPadre de {x.key}: None")
    print()
