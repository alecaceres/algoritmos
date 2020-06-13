from inpHeXionWindow import start_window

def main(window):
    board = []
    for i in range(7):
        board.append([])
        for j in range(7):
            board[i].append(0)

    board[3][2] = 0 # celda vacia
    board[3][3] = 1 # ficha blanca
    board[3][4] = 2 # ficha negra

    # imprimir tablero en la venta
    window.print_board(board)

    while(True):


        # capturar la posicion de la celda seleccionada con el click del mouse
        print('Haga click sobre la celda para imprimir el indice de la celda correspondiente.')
        pos = window.scan_position()
        print('Click en la celda (' + str(pos[0]) + ', ' + str(pos[1]) + ')')

        whites_turn = True
        if turno_blanco:
            board[pos[0]][pos[1]] = 1

            # imprimir tablero en la venta
            window.print_board(board)

        # cerrar la ventana (si elimina esta linea, la ventana se debera cerrarse manualmente)
    window.close()


# iniciar el programa
start_window(main)
