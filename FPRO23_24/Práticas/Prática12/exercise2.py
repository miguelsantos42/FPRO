def wins(board, row, col, player):
    if board[row] == 3*[player]:  # Ganha pelas linhas
        return True
    if [board[r][col] for r in range(3)] == 3*[player]:  # Ganha pelas colunas
        return True
    if [board[i][i] for i in range(3)] == 3 * [player]:  # Ganha pela diagonal
        return True
    if [board[i][2-i] for i in range(3)] == 3 * [player]:  # Ganha pela diagonal inversa
        return True
    return False

def tic_tac_toe(board, player):
    matrix = []
    linhas = board.split('\n')
    for row in linhas:
        matrix.append(list(row))
    for row in range(3):
        for col in range(3):
            if matrix[row][col] == ' ':
                matrix[row][col] = player
                if wins(matrix, row, col, player):
                    return(chr(ord('A') + row) + str(col+1))
                matrix[row][col] = ' '  # This line should correctly reset the cell to ' '


# print(tic_tac_toe(' xx\n o \noxo', 'x'))
# print(tic_tac_toe('xo \n xo\no  ', 'x'))
# print(tic_tac_toe('x x\n o \nxoo', 'o'))
# print(tic_tac_toe('xx \n ox\n oo', 'o'))
