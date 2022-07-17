class Dot:
    neighbours = []

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def connect_dot(self, neighbour, c):
        self.neighbours.append([neighbour, c])


class Player:
    points = 0

    def __init__(self, c):
        self.color = c

    def add_point(self):
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
            if dot.i == m1 and dot.j == k1:
                for neighbour in self.dots:
                    if neighbour.i == m2 and neighbour.j == k2:
                        dot.connect_dot(neighbour, c)
                        neighbour.connect_dot(dot, c)
                        self.lines.add({dot, neighbour, c})


n = int(input('number of playes: '))
m, k = input('ground dimensions: ').split()

ground = Ground(int(m), int(k))

players = []
for i in range(n):
    players.append(Player(i+1))
