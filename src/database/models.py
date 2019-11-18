"""N Queen Puzzle models"""

from sqlalchemy import Column, Integer, ARRAY

from .sessions import Base


class Solution(Base):
    """N Queen Puzzle solution model"""
    __tablename__ = 'solutions'

    id = Column(Integer, primary_key=True)
    n = Column(Integer)
    solution = Column(ARRAY(Integer, dimensions=2))

    def __init__(self, n, solution):
        self.n = n
        self.solution = solution


class SolutionQuery(Base):
    """Saves if a n has been queried"""
    __tablename__ = 'solution_queries'

    id = Column(Integer, primary_key=True)
    n = Column(Integer)
    status = Column(Integer)

    def __init__(self, n, status):
        self.n = n
        self.status = status
