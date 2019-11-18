"""Solver testing"""

import unittest

from ..solutions import ensure_queen, solve_puzzle


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
        self.assertFalse(ensure_queen(board, 1, 3, 4))

    def test_ensure_queen_wrong_diagonal(self):
        """Make sure that ensure_queen function works for diagonals"""
        board = [
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
            [0, 1, 0, 0],
        ]
        self.assertFalse(ensure_queen(board, 2, 3, 4))

    def test_ensure_queen_right_board(self):
        """Make sure that ensure_queen function works for right boards"""
        board = [
            [0, 0, 1, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 0, 0],
        ]
        self.assertTrue(ensure_queen(board, 2, 3, 4))

    def test_solve_puzzle_solution_number(self):
        """Ensures we are getting all solutions"""
        n_1 = len([board for board in solve_puzzle(1)])
        n_2 = len([board for board in solve_puzzle(2)])
        n_4 = len([board for board in solve_puzzle(4)])
        n_5 = len([board for board in solve_puzzle(5)])

        self.assertEqual(n_1, 1)
        self.assertEqual(n_2, 0)
        self.assertEqual(n_4, 2)
        self.assertEqual(n_5, 10)

    def test_solve_puzzle_solutions(self):
        """Ensures given solutions are correct"""
        solutions = [
            [
                [0, 0, 1, 0],
                [1, 0, 0, 0],
                [0, 0, 0, 1],
                [0, 1, 0, 0],
            ],
            [
                [0, 1, 0, 0],
                [0, 0, 0, 1],
                [1, 0, 0, 0],
                [0, 0, 1, 0],
            ]
        ]

        for solution in solve_puzzle(4):
            self.assertIn(solution, solutions)


if __name__ == "__main__":
    unittest.main()
