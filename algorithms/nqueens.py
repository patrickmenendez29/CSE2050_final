# functions that solve the nqueens algorithm

# @desc: function that checks if a cell is valid to place a queen or not
# @params:
#   board: matrix or 2D list of the board (values need to be either 1 or 0)
#   row: index of row in which the cell is located
#   col: index of column in which the cell is located
# @returns: True if the cell can be placed, False otherwise
def is_cell_valid(board, row, col):
    n = len(board)

    # check if there is a queen in row or column
    for i in range(0, n):
        # if there is a queen in the same col or the same row
        if board[row][i] == 1 or board[i][col] == 1:
            return False

    # checking diagonals by traversing the whole grid and matching the postitive/negative diagonally adjacent cells
    for i in range(0, n):
        for j in range(0, n):
            # if there is a queen in the positive or negative diagonal
            if (i + j == row + col) or (i - j == row - col):
                if board[i][j] == 1:
                    return False
    return True


# @desc: solve the n-queens problem in a n by n board
# @params:
#   board: matrix or 2D list of the board (values need to be either 1 or 0)
#   col: must be 0 ( to access it recursively)
# @returns: a board with 1's placed where queens are supposed to be, False if there's no solution
def get_solution(board, col):
    n = len(board)

    # base case: the board is already solved
    if col >= n:
        return board

    # traverse through the board and solve it using backtracking and recursion
    for i in range(n):
        # if the cell is a valid place for a queen, place one
        if is_cell_valid(board, i, col):
            board[i][col] = 1

            # if there is still a solution, use the function again but with the next column
            if get_solution(board, col + 1):
                # return the solved board
                return board

            board[i][col] = 0
    # if there is no solution, return False
    return False

# test the algorithms
if __name__ == '__main__':
    board = [
        [0, 0],
        [0, 0]
    ]
    board = get_solution(board, 0)

    print(board)
