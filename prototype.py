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

def check_neighbours(row_index, column_index, board):
    neighbours = 0

    directions = [
        [-1,-1], [-1, 0], [-1, 1],
        [ 0,-1],          [ 0, 1],
        [ 1,-1], [ 1, 0], [ 1, 1]
    ]
    
    rows = len(board)
    columns = len(board[0])

    for direction in directions:
        neighbour_row = row_index + direction[0]
        neighbour_column = column_index + direction[1]

        if 0 <= neighbour_row < rows and 0 <= neighbour_column < columns:
            if board[neighbour_row][neighbour_column] == 'X':
                neighbours += 1

    return neighbours

def update_board(board):
    new_board = [['O'] * len(board[i]) for i in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[i])):
            neighbour_count = check_neighbours(i, j, board)
            if neighbour_count == 2 and board[i][j] == 'X':
                new_board[i][j] = 'X'
            elif neighbour_count == 3:
                new_board[i][j] = 'X'

            
    return new_board

def write_board(board):
    with open('board.txt', 'w') as f:
        for line in board:
            f.write(''.join(line) + '\n')

choice = False
while not choice:
    print_board(board)
    board = update_board(board)
    # write_board(board)
    choice = input('Enter to continue ')
