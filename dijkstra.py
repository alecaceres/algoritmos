import heap

def dijkstra(G, s):
    G.InitializeSingleSource(s)
    S = set()
    Q = heap.HeapVector(G.nodes.copy())
    i = 0
    while Q.heap_size:
        i+=1
        u = Q.ExtractMin()
        S.add(u)
        for (v, w) in u.neighbours:
            heap.Relax(u, v, w)
            if v not in S: Q.HeapDecreaseKey(Q.queue.index(v), v)
G = heap.yaml2graph()
for node in G.nodes:
    dijkstra(G, node)
    for x in G.nodes:
        if x != node:
            try: print(f"Distancia de {node.key} a {x.key}\t: {x.d}.\t\tPadre de {x.key}: {x.pi.key}")
            except: print(f"Distancia de {node.key} a {x.key}\t: {x.d}.\t\tPadre de {x.key}: None")
    print()
