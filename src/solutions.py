"""Queens puzzle solver using backtracking"""

import copy


def ensure_queen(board, row, col, n):
    """Returns True if queen is safe, otherwise returns False"""

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
    for i, j in zip(range(row, n, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_puzzle_util(board, col, n):
    """Generates every board solution"""
    # If we reached last column, yields that solution
    if (col == n):
        yield copy.deepcopy(board)
    # If we haven't reached last column, we must continue
    else:
        for row in range(n):
            if ensure_queen(board, row, col, n):
                board[row][col] = 1

                for solution in solve_puzzle_util(board, col + 1, n):
                    yield solution
                board[row][col] = 0


def solve_puzzle(n):
    """Given an n, returns all possible solutions for a n size board"""
    board = [[0 for _ in range(n)] for _ in range(n)]

    for solution in solve_puzzle_util(board, 0, n):
        yield solution
