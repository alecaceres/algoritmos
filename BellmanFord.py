import heap

def BFShortestPaths(G, s):
    for i in range(len(G.nodes)):
        for u in G.nodes:
            for (v, w) in u.neighbours:
                heap.Relax(u, v, w)
    for u in G.nodes:
        for (v, w) in u.neighbours:
            if v.d > u.d + w: return False
    return True

G = heap.yaml2graph(path = 'input_BellmanFord.yaml')
for node in G.nodes:
    graph = G
    if BFShortestPaths(G, node):
        for x in G.nodes:
            if x != node:
                try: print(f"Distancia de {node.key} a {x.key}\t: {x.d}.\t\tPadre de {x.key}: {x.pi.key}")
                except: print(f"Distancia de {node.key} a {x.key}\t: {x.d}.\t\tPadre de {x.key}: None")
    else: print(f"Existe un ciclo de peso negativo con la fuente {node.key}")
    print()
