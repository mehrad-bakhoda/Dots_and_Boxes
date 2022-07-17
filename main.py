class Dot:
    neighbours = []

    def __init__(self, i, j):
        self.i = i
        self.j = j


class Line:
    def __init__(self, p1, p2, c):
        self.p1 = p1
        self.p2 = p2
        self.color = c


class Player:
    points = 0

    def __init__(self, c):
        self.color = c

    def addPoint(self):
        self.points += 1


class Ground:
    dots = []
    lines = set()
    dotsGround = []

    def __init__(self, m, k):
        self.m = m
        self.k = k

        for i in range(m):
            self.dots.append(k * [])
            for j in range(k):
                self.dots[i][j] = Dot(i, j)

    def drawLine(self, m1, m2, k1, k2, c):
        dot = self.dots[m1][k1]
        neighbour = self.dots[m2][k2]

        if not (Line(dot, neighbour, c) in self.lines) and not (Line(neighbour, dot, c) in self.lines):
            self.lines.add(Line(dot, neighbour, c))


def checkGame(ground, dots, lines, lastLine):
    lastColor = lastLine.color

    if (Line(dots[lastLine.p1.i][lastLine.p1.j + 1], dots[lastLine.p2.i][lastLine.p2.j + 1]) in lines
            or
            Line(dots[lastLine.p2.i][lastLine.p2.j + 1],
                 dots[lastLine.p1.i][lastLine.p1.j + 1]) in lines
    ):
        ground.drawLine(lastLine.p1.i, lastLine.p1.j + 1,
                        lastLine.p2.i, lastLine.p2.j + 1, lastColor)
        players[lastColor].addPoint()

    if (Line(dots[lastLine.p1.i][lastLine.p1.j - 1], dots[lastLine.p2.i][lastLine.p2.j - 1]) in lines
            or
            Line(dots[lastLine.p2.i][lastLine.p2.j - 1],
                 dots[lastLine.p1.i][lastLine.p1.j - 1]) in lines
    ):
        ground.drawLine(lastLine.p1.i, lastLine.p1.j - 1,
                        lastLine.p2.i, lastLine.p2.j - 1, lastColor)
        players[lastColor].addPoint()

    if (Line(dots[lastLine.p1.i + 1][lastLine.p1.j], dots[lastLine.p2.i + 1][lastLine.p2.j]) in lines
            or
            Line(dots[lastLine.p2.i + 1][lastLine.p2.j],
                 dots[lastLine.p1.i + 1][lastLine.p1.j]) in lines
    ):
        ground.drawLine(lastLine.p1.i + 1, lastLine.p1.j,
                        lastLine.p2.i + 1, lastLine.p2.j, lastColor)
        players[lastColor].addPoint()

    if (Line(dots[lastLine.p1.i - 1][lastLine.p1.j], dots[lastLine.p2.i - 1][lastLine.p2.j]) in lines
            or
            Line(dots[lastLine.p2.i - 1][lastLine.p2.j],
                 dots[lastLine.p1.i - 1][lastLine.p1.j]) in lines
    ):
        ground.drawLine(lastLine.p1.i - 1, lastLine.p1.j,
                        lastLine.p2.i - 1, lastLine.p2.j, lastColor)
        players[lastColor].addPoint()


n = int(input('number of playes: '))
m, k = int(input('ground dimensions: ').split())

ground = Ground(m, k)
players = []
for i in range(n):
    players.append(Player(i + 1))

# now we will get coordinates from each player and play the game until there are no lines left