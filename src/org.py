from pos import Pos

class Gene:
    pass

class Organism(): 
    def __init__(self, x: float, y: float, speed: float, vrange: float):
        self.pos = Pos(x, y)
        self.speed = speed
        self.vrange = vrange
        self.food = 0

    def __init__(self, pos: Pos, speed: float, vrange: float):
        self.pos = pos
        self.speed = speed
        self.vrange = vrange
        self.food = 0

    def setDest(self, dest: Pos):
        self.dest = dest

    def calcFitness(self):
        pass

    def move(self) -> bool:
        dist = self.pos.dist(self.dest)
        if (dist < speed):
            self.pos.x = self.dest.x
            self.pos.y = self.dest.y
            self.dest = None
            return True
        else:
            self.pos.x = self.pos.x + (self.dest.x - self.pos.x) * speed / dist
            self.pos.y = self.pos.y + (self.dest.y - self.pos.y) * speed / dist
            return False

    def consume(self):
        self.food = self.food + 1

    def gene(self) -> Gene:
        pass
