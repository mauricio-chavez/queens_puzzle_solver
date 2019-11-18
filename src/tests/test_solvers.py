"""Solver testing"""

import unittest

from ..solutions import ensure_queen


class SolverTestCase(unittest.TestCase):
    """Contains every test about solvers"""

    def test_ensure_queen_wrong_row(self):
        """Make sure that ensure_queen function works for rows"""
        board = [
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
            [0, 1, 0, 0],
        ]
        self.assertFalse(ensure_queen(board, 1, 3))

    # @unittest.skip('Diagonals not implemented')
    def test_ensure_queen_wrong_diagonal(self):
        """Make sure that ensure_queen function works for diagonals"""
        board = [
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
            [0, 1, 0, 0],
        ]
        self.assertFalse(ensure_queen(board, 2, 3))

    # @unittest.skip('Not accurate')
    def test_ensure_queen_right_board(self):
        """Make sure that ensure_queen function works for right boards"""
        board = [
            [0, 0, 1, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 0, 0],
        ]
        self.assertTrue(ensure_queen(board, 2, 3))


if __name__ == "__main__":
    unittest.main()
