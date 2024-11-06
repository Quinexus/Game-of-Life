# Prototyping Conway's game of life in python

### Rules
# underpopulation <2 neighbours dies
# lives with 2 or 3 neighbours
# overpopulation >3 neighbours dies
# reproduction dead with =3 neighbours lives
with open('board.txt', 'r') as f:
    board = [[char.strip('') for char in line.strip('\n')] for line in f]

def print_board(board):
    for line in board:
        print(''.join(line))

def check_neighbours(line_index, cell_index, board):
    neighbours = 0

    # Checking top cell = line - 1
    if line_index != 0:
        if board[line_index-1][cell_index] == 'X':
            neighbours += 1
    # Checking right top cell = line - 1 & cell + 1
    if (line_index != 0) & (cell_index != len(board[line_index - 1]) - 1):
        if board[line_index - 1][cell_index + 1] == 'X':
            neighbours += 1
    # Checking right cell = cell + 1
    if cell_index != len(board[line_index]) - 1:
        if board[line_index][cell_index + 1] == 'X':
            neighbours += 1
    # Checking right bottom cell = line + 1 & cell + 1
    if (line_index != len(board) - 1) & (cell_index != len(board[line_index]) - 1):
        if board[line_index + 1][cell_index + 1] == 'X':
            neighbours += 1

    # Checking bottom cell = line + 1
    if line_index != len(board) - 1:
        if board[line_index + 1][cell_index] == 'X':
            neighbours += 1
    # Checking left bottom cell = line + 1 & cell - 1
    if (line_index != len(board) - 1) & (cell_index > 0):
        if board[line_index + 1][cell_index - 1] == 'X':
            neighbours += 1
    # Checking left cell = cell - 1
    if cell_index > 0:
        if board[line_index][cell_index - 1] == 'X':
            neighbours += 1
    # Checking left top cell = line - 1 & cell - 1
    if (cell_index > 0) & (line_index > 0):
        if board[line_index - 1][cell_index -1] == 'X':
            neighbours += 1
    
    return neighbours


def update_board(board):
    new_board = [['O' for i in range(len(board[0]))] for j in range (len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            neighbour_count = check_neighbours(i, j, board)
            if neighbour_count == 2 and board[i][j] == 'X':
                new_board[i][j] = 'X'
            elif neighbour_count == 3:
                new_board[i][j] = 'X'
            else:
                new_board[i][j] = 'O'
    return new_board

def write_board(board):
    with open('board.txt', 'w') as f:
        for line in board:
            f.write(''.join(line) + '\n')


x = 's'
while x != 'q':
    print_board(board)
    board = update_board(board)
    write_board(board)
    input('step')
