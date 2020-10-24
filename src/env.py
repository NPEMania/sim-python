from pop import Population
from pos import Pos

class Env:
    def __init__(self):
        self.pop = Population.generatePop(Pos.getRandomPosList(0.0, 0.0, 100.0, 100.0), 10.0, 2.0)
        self.food: list[Pos] = Pos.getRandomPosList(0.0, 0.0, 100.0, 100.0)