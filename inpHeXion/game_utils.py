import networkx as nx
from networkx.algorithms.shortest_paths.generic import has_path
import itertools
import random
import json

config = json.load(open('config.json'))

def addNode(G, node):
    '''
    Función llamada para inicializar cada nodo con player 0.
    '''
    i,j = node
    G.add_node(i+j*7)
    return G

def addFirstPlayer(G, dest, player):
    '''
    Función llamada para agregar al primer jugador en el tablero.
    '''
    i,j = dest
    G.nodes[i+j*7]['player'] = player
    G = addEdges(G, *dest, player)
    return G, getBoard(G)

def addPlayer(G, src, dest, player):
    '''
    G:      Grafo del tablero
    src:    Posición de la ficha del rival por mover
    dest:   Posición a la cual la ficha del rival quiere moverse
    player: El que realiza la jugada
    '''
    i_src, j_src = src # nodo de origen (donde se hace el primer clic)
    i_dest, j_dest = dest # nodo de destino (donde se hace el segundo clic)
    src_pos = i_src+j_src*7 # posición del origen en notación vectorial (no matricial)
    dest_pos = i_dest+j_dest*7 # posición del destino en notación vectorial (no matricial)
    G.nodes[src_pos]['player'] = player # el nodo del origen se queda pintado en el color del player
    G.nodes[dest_pos]['player'] = 1 if player==2 else 2 # el nodo de destino se queda pintado en el color del rival
    G.remove_edge(src_pos, dest_pos, key = 'possible_movement') # se elimina la arista src_dest como posible mov.
    G = updatePlayers(G, src_pos, src, player)
    G.remove_edges_from([edge for edge in G.edges(dest_pos) if G.has_edge(*edge, key = 'possible_movement')])
    G = addEdges(G, *dest, player)
    return G, getBoard(G)

def addEdges(G, i, j, player):
    '''
    Función para agregar aristas luego de una jugada.
    '''
    possible_movements = {(i,j+1),(i,j-1),(i+1,j),(i-1,j),(i-1,j+1),(i+1,j-1)}
    possible_movements = [(i+j*7,
                           movement[0] + movement[1]*7,
                           G.nodes[movement[0]+movement[1]*7]['player']
                           ) for movement in possible_movements if movement
                           in [(i,j) for i in range(7) for j in range(7)]] # si la posición existe en el tablero
    [G.add_edge(i,j, key = 'possible_movement') for (i,j,p) in possible_movements if not p]
    [G.add_edge(i,j, key = 'path') for (i,j, p) in possible_movements if p and p!=player]
    return G

def updatePlayers(G, src_pos, src, player):
    '''
    Se actualizan las aristas (tienen la etiqueta de possible_movement si
    puede mover del nodo fuente al nodo destino y la etiqueta de path si
    forma un camino para uno de los jugadores).
    '''
    i,j = src
    path_edges = {(i,j+1),(i,j-1),(i+1,j),(i-1,j),(i-1,j+1),(i+1,j-1)}
    path_edges = [(i+j*7, movement[0] + movement[1]*7)
                            for movement in path_edges
                            if (movement in [(i,j) for i in range(7) for j in range(7)] # si la posición existe en el tablero
                                and G.nodes[movement[0]+movement[1]*7]['player'] == player)]
    G.remove_edges_from([edge for edge in G.edges(src_pos) if not G.has_edge(*edge, key = 'possible_movement')])
    [G.add_edge(i,j, key = 'path') for (i,j) in path_edges]
    return G

def hasWon(G, player):
    '''
    Esta función devuelve un booleano para saber si el jugador ha
    ganado la partida.
    '''
    G = G.copy()
    G.remove_edges_from([edge for edge in G.edges if 'possible_movement' in edge])
    all_possible_paths = (list(itertools.product(range(7), range(41,49))
                        if player == 2 else list(itertools.product(range(0,49,7), range(6,49,7)))))
    return any([has_path(G, src, dest)
                for (src, dest) in all_possible_paths
                if (G.nodes[src]['player'] == player and G.nodes[dest]['player'] == player)])

def getPossibleMovements(G, player):
    '''
    Retorna una lista con las jugadas posibles.
    '''
    edges = [edge for edge in G.edges]
    edges.extend([(y,x,attr) for (x,y,attr) in edges])
    return [edge[1::-1] for edge in edges
            if (G.nodes[edge[0]]['player'] == (1 if player==2 else 2)
               and 'possible_movement' in edge)]

def nextBlackMovement(G):
    '''
    Esta función se encarga de implementar la lógica de la siguiente
    jugada del jugador negro.
    '''
    val_max = float('-inf')
    src_max = dest_max = None
    for (src, dest) in getPossibleMovements(G, player = 2):
        dest, src = (dest, src) if G.nodes[dest]['player'] != 1 else (src, dest)
        val_max, src_max, dest_max = max((val_max, src_max, dest_max),
                                        (minimax(simulateMovement(G,src,dest,player=2),
                                        depth = config['depth']),
                                        src, dest), key = lambda x: x[0])
    return (src_max%7, src_max//7), (dest_max%7, dest_max//7)

def simulateMovement(G,src,dest,player):
    G_copy = G.copy()
    G_copy, _ = addPlayer(G_copy, (src%7, src//7), (dest%7, dest//7), player)
    return G_copy

def minimax(G, depth, alpha = float('inf'),
            beta = float('-inf'), maximisingPlayer = True):
    if not depth: # or game over
        return heuristic(G, player = int(maximisingPlayer)+1)

    if maximisingPlayer:
        maxEval = float('-inf')
        for (src, dest) in getPossibleMovements(G, player = 1):
            dest, src = (dest, src) if G.nodes[dest]['player'] != 2 else (src, dest)
            eval = minimax(simulateMovement(G,src,dest,player=1), depth-1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha: break
        return maxEval
    else:
        minEval = float('inf')
        for (src, dest) in getPossibleMovements(G, player = 2):
            dest, src = (dest, src) if G.nodes[dest]['player'] != 1 else (src, dest)
            eval = minimax(simulateMovement(G,src,dest,player=2), depth-1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha: break
        return minEval

def heuristic(G, player):
    '''
    Devuelve el diámetro de la componente conectada de mayor diámetro.
    Para ello, se considera solamente al grafo con los nodos iguales al jugador.
    '''
    G = G.copy()
    G.remove_edges_from([edge for edge in G.edges if 'possible_movement' in edge])
    G.remove_nodes_from([node for node in G.nodes if G.nodes[node]['player']!=player])
    largest_cc = max((G.subgraph(g) for g in nx.connected_components(G)), default = 0,
                     key = nx.algorithms.distance_measures.diameter)
    return len(largest_cc)

def getBoard(G):
    return [[G.nodes[i+j*7]['player'] for j in range(7)] for i in range(7)]
