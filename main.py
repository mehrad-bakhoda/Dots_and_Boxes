class Dot:
    neighbours = []

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def connectDot(self, neighbour, c):
        self.neighbours.append([neighbour, c])


class Player:
    points = 0

    def __init__(self, c):
        self.color = c

    def addPoint(self):
        self.points += 1


class Ground:
    dots = []
    lines = set()

    def __init__(self, m, k):
        self.m = m
        self.k = k

        for i in range(m):
            for j in range(k):
                self.dots.append(Dot(i, j))

    def drawLine(self, m1, m2, k1, k2, c):
        for dot in self.dots:
            if (dot.i == m1 and dot.j == k1):
                for neighbour in self.dots:
                    if (neighbour.i == m2 and neighbour.j == k2):
                        dot.connectDot(neighbour, c)
                        neighbour.connectDot(dot, c)
                        self.lines.add({dot, neighbour, c})


n = int(input('number of playes: '))
m, k = int(input('ground dimensions').split())

ground = Ground(m, k)

players = []
for i in range(n):
    players.append(Player(i+1))
