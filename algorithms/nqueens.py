

def is_cell_valid(board, row, col):
    n = len(board)

    for i in range(n):
        if board[row][i] == 1:
            return False

    for i in range(n):
        if board[i][col] == 1:
            return False

    for x, y in zip(range(row, n), range(col, n)):
        if board[x][y] == 1:
            print("cannot place queen because there is a queen in (%s, %s) already [SE]" % (x, y))
            return False

    for x, y in zip(range(row, 0, -1) ,range(col, 0, -1)):
        if board[x][y] == 1:
            print("cannot place queen because there is a queen in (%s, %s) already [NW]" % (x, y))
            return False

    for x, y in zip(range(row, n), range(col, 0, -1)):
        if board[x][y] == 1:
            print("cannot place queen because there is a queen in (%s, %s) already [NE]" % (x, y))
            return False

    for x, y in zip(range(row, 0, -1), range(col, n)):
        if board[x][y] == 1:
            print("cannot place queen because there is a queen in (%s, %s) already [SW]" % (x, y))
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
