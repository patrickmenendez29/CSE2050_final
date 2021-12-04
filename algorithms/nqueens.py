

def is_cell_valid(board, row, col):
    n = len(board)

    for i in range(col):
        if board[row][i] == 1:
            return False

    for x in range(row, -1, -1):
        for y in range(col, -1, -1):
            if board[x][y] == 1:
                return False

    for x in range(row, n, 1):
        for y in range(col, -1, -1):
            if board[x][y] == 1:
                return False

    return True


def get_solution(board, col):

    n = len(board)

    if col >= n:
        return True

    for i in range(n):
        if is_cell_valid(board, i, col):
            board[i][col] = 1

            if get_solution(board, col + 1):
                return True

            board[i][col] = 0

    return False
