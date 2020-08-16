from inpHeXionWindow import start_window
from black_player import next_movement
from game_utils import playerStatus
import time

def main(window):
    board = []
    for i in range(7):
        board.append([])
        for j in range(7):
            board[i].append(0)
    board = [[0]*7 for i in range(7)]

    # imprimir tablero en la venta
    window.print_board(board)

    # la primera vez se puede colocar la ficha en cualquier parte
    print('Haga click sobre la celda para imprimir el indice de la celda correspondiente.')
    pos = window.scan_position()
    board[pos[0]][pos[1]] = 1
    print('Click en la celda (' + str(pos[0]) + ', ' + str(pos[1]) + ')')
    window.print_board(board) # imprimir tablero en la venta

    while(True):
        playerStatus(board, 2)
        # turno de la ficha negra
        time.sleep(1)
        board = next_movement(board)
        window.print_board(board)
        playerStatus(board, 1)
        while True:
            pos = window.scan_position()
            if board[pos[0]][pos[1]] != 2: # solo se puede elegir una celda con ficha negra
                print('Celda no válida')
            else:
                print(f'Click en la celda ({pos[0]}, {pos[1]})')
                print('Indique la celda a la cual la ficha negra debe moverse')
                while True:
                    pos_move = window.scan_position()
                    print(abs(pos[0]-pos_move[0]) + abs(pos[1]-pos_move[1]))
                    i,j = pos
                    possible_movements = {(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i+1,j-1),(i-1,j+1)}
                    possible_movements = [movement for movement in possible_movements
                                        if not board[movement[0]][movement[1]]]
                    if pos_move not in possible_movements:
                        print('Celda no válida')
                    else:
                        board[pos_move[0]][pos_move[1]] = 2
                        board[pos[0]][pos[1]] = 1
                        window.print_board(board) # imprimir tablero en la venta
                        break
                break # turno de la ficha negra


    window.close()


# iniciar el programa
start_window(main)
