# Prototyping String List Version GOL (more compatible to transfer to BASH)

### Rules
# underpopulation <2 neighbours dies
# lives with 2 or 3 neighbours
# overpopulation >3 neighbours dies
# reproduction dead with =3 neighbours lives

with open('board.txt', 'r') as f:
    board = [line.strip('\n') for line in f]

def print_board(board):
    for line in board:
        print(line)

row_count= len(board)
column_count = len(board[0])

def check_neighbours(row_index, column_index, board):
    neighbours = 0

    directions = [
        [-1,-1], [-1, 0], [-1, 1],
        [ 0,-1],          [ 0, 1],
        [ 1,-1], [ 1, 0], [ 1, 1]
    ]

    for direction in directions:
        neighbour_row = row_index + direction[0]
        neighbour_column = column_index + direction[1]

        if 0 <= neighbour_row < row_count and 0 <= neighbour_column < column_count:
            if board[neighbour_row][neighbour_column] == 'X':
                neighbours += 1

    return neighbours

def update_board(board):
    new_board = []

    for i in range(len(board)):
        new_row = ""

        for j in range(len(board[i])):
            neighbour_count = check_neighbours(i, j, board)

            if neighbour_count == 2 and board[i][j] == 'X':
                new_row += "X"
            elif neighbour_count == 3:
                new_row += "X"
            else:
                new_row += "O"
            
        new_board.append(new_row)
            
    return new_board

def write_board(board):
    with open('board.txt', 'w') as f:
        for line in board:
            f.write(line + '\n')

choice = False
while not choice:
    print_board(board)
    board = update_board(board)
    # write_board(board)
    choice = input('Enter to continue ')
