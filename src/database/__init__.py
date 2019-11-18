"""Project database manager"""

from .sessions import session_factory
from .models import Solution


def create_solution(n, solution):
    """Inserts a solution row into database"""
    session = session_factory()
    solution = Solution(n, solution)
    session.add(solution)
    session.commit()
    session.close()
