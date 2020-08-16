'''
Este módulo está dedicado a modelar el comportamiento del jugador negro
'''

def next_movement(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                board[i+1][j] = 1
                board[i][j] = 2
                return board
