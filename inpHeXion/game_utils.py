def checkWinner(board):
    players = (None, 'white', 'black')
    winner = []
    for player in {1, 2}: winner.append(board, player)
    return winner

def playerStatus(board, player):
    to_check_u = [(0, pos) for pos,value in enumerate(board[0]) if value == player]
    to_check_l = [(pos, 0) for pos,value in enumerate(list(zip(*board))[0]) if value == player]
    for top in to_check_u:
        if solveMaze(board, top, player, goal = (6, None)): return True
        print('hola, bienvenido a player status')
    for left in to_check_l:
        if solveMaze(board, left, player, goal = (None, 6)): return True
    return False # si no existe camino entre lados opuestos

def pathExists(board, pos, player, goal):
    i,j = pos
    if board[i][j] != player: return False
    if i == goal[0] or j == goal[1]: return True
    possible_movements = {(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i+1,j-1),(i-1,j+1)}
    if goal[1] is None:
        possible_movements.remove((i-1, j))
        possible_movements.remove((i-1, j+1))
    elif goal[0] is None:
        possible_movements.remove((i, j-1))
        possible_movements.remove((i+1, j-1))

def solveMaze(board, pos, player, goal):
    print('empanada')
    print(pos)
    x_goal, y_goal = goal
    x_pos, y_pos = pos
    sol = [ [ 0 for j in range(7) ] for i in range(7) ]

    if solveMazeUtil(board, x_pos, y_pos, sol, x_goal, y_goal, player):
        print("solution does exist")
        return True
    print("Solution doesn't exist");
    return False

def isSafe(maze, x, y, player):

    if x >= 0 and x < 7 and y >= 0 and y < 7 and maze[x][y] == player:
        return True

    return False

def solveMazeUtil(maze, x, y, sol, x_goal, y_goal, player):
    print("estoy en", x, y, "\t goal", x_goal, y_goal)
    if x == x_goal or y == y_goal:
        sol[x][y] = 1
        print('ya es si que true')
        return True
    print('no es true')
    if isSafe(maze, x, y, player) == True:
        print("sol[x][y]", x, y)
        sol[x][y] = 1
        if solveMazeUtil(maze, x + 1, y, sol, x_goal, y_goal, player) == True:
            return True
        if solveMazeUtil(maze, x, y + 1, sol, x_goal, y_goal, player) == True:
            return True
        sol[x][y] = 0
        return False
