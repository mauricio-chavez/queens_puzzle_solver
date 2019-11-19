"""Project utils"""

from database import create_solution, session_factory, SolutionQuery
from solutions import solve_puzzle


def save_solutions(n):
    """Solution saver"""
    for solution in solve_puzzle(n):
        create_solution(n, solution)

    session = session_factory()
    solution = session.query(SolutionQuery).filter_by(n=n).first()
    solution.status = 2
    session.commit()
    session.close()
