from math import sqrt
from random import uniform as unf

class Pos:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'x = {self.x}, y = {self.y}'

    def dist(self, other: Pos) -> float:
        return sqrt((self.x - other.x) * (self.x - other.x) + (self.y - other.y) * (self.y - other.y))

    @staticmethod
    def getRandomPosList(xmin: float, ymin: float, xmax: float, ymax: float, size: int) -> list[Pos]:
        positions: list[Pos] = []
        for i in range(size):
            positions.append(Pos(unf(xmin, xmax), unf(ymin, ymax)))
        return positions
