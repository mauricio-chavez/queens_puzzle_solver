"""Project database manager"""

from .sessions import _SessionFactory, Base, engine
from .models import Solution, SolutionQuery


def session_factory():
    """Retrives sessions"""
    Base.metadata.create_all(engine)
    return _SessionFactory()


def create_solution(n, solution):
    """Inserts a solution row into database"""
    session = session_factory()
    solution = Solution(n, solution)
    session.add(solution)
    session.commit()
    session.close()


def create_solution_query(n, status):
    """Inserts a solution query row into database"""
    session = session_factory()
    solution_query = SolutionQuery(n, status)
    session.add(solution_query)
    session.commit()
    session.close()
