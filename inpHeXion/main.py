from inpHeXionWindow import start_window
from game_utils import *
import time
import networkx as nx

def main(window):
    '''
    Player 1: Blanco
    Player 2: Negro
    Player 0: Default, sin jugador
    '''
    G = nx.MultiGraph()
    G.add_nodes_from(range(49), player = 0)
    board = getBoard(G)

    # imprimir tablero en la venta
    window.print_board(board)

    # la primera vez se puede colocar la ficha en cualquier parte
    pos = window.scan_position()
    G, board = addFirstPlayer(G, pos, 1)
    window.print_board(board) # imprimir tablero en la venta

    while(True):
        if hasWon(G, player = 1):
            print("Ganó el jugador blanco")
            time.sleep(60)
            break
        # turno de la ficha negra
        src, dest = nextBlackMovement(G)
        G, board = addPlayer(G, src, dest, 2)
        window.print_board(board)
        if hasWon(G, player = 2):
            print("Ganó el jugador negro")
            time.sleep(60)
            break
        while True:
            pos = window.scan_position()
            if board[pos[0]][pos[1]] != 2: # solo se puede elegir una celda con ficha negra
                print('Celda no válida')
            else:
                while True:
                    pos_move = window.scan_position()
                    possible_movements = [(node%7, node//7) for edge in
                                            getPossibleMovements(G, player = 1)
                                            for node in edge
                                            if pos[0]+pos[1]*7 in edge]
                    if pos_move not in possible_movements or pos_move == pos:
                        print('Celda no válida')
                    else:
                        G, board = addPlayer(G, pos, pos_move, 1)
                        window.print_board(board) # imprimir tablero en la venta
                        break
                break # turno de la ficha negra


    window.close()


# iniciar el programa
start_window(main)
