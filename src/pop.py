from org import Organism
from pos import Pos
from random import uniform as unf

class Population:
    def __init__(self, orgs: list[Organism]):
        self.orgs = orgs
    
    def fittest(self) -> Organism:
        pass

    @staticmethod
    def generatePop(pos: list[Pos], maxspeed: float, maxvrange: float) -> Population:
        orgs: list[Organism] = []
        for p in pos:
            orgs.append(Organism(p, unf(1.0, maxspeed), unf(0.0, maxvrange)))
        return Population(orgs)