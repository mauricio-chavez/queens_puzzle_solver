"""Queens puzzle solver using backtracking"""


def ensure_queen(board, row, col):
    """Returns True if queen is safe, otherwise returns False"""
    N = len(board)

    # Check this row on left side since there's no need of checking right side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True
