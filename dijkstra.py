import heap

def dijkstra(G, s):
    G.InitializeSingleSource(s)
    S = set()
    Q = heap.HeapVector(G.nodes.copy())
    while Q.heap_size:
        u = Q.ExtractMin()
        S.add(u)
        for (v, w) in u.neighbours:
            heap.Relax(u, v, w)

G = heap.yaml2graph()
for node in G.nodes:
    graph = G
    dijkstra(G, node)
    for x in G.nodes:
        if x != node:
            try: print(f"Distancia de {node.key} a {x.key}\t: {x.d}.\t\tPadre de {x.key}: {x.pi.key}")
            except: print(f"Distancia de {node.key} a {x.key}\t: {x.d}.\t\tPadre de {x.key}: None")
    print()
