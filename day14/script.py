#!/usr/bin/env python3
formations =  open(0).read().strip().split("\n")
class Cave:
    def __init__(self, forms):
        self.rocks = set()
        self.sand_source = (500,0)
        for f in forms:
            points = [list(map(int, x.split(","))) for x in f.split(" -> ")]
            for i in range(len(points)-1):
                (x1,y1) = points[i]
                (x2, y2) = points[i+1]
                for x in range(min(x1,x2),max(x1,x2)+1):
                    for y in range(min(y1,y2),max(y1,y2)+1):
                        self.rocks.add((x,y))
        self.abyss = max([y for (_,y) in self.rocks]) + 1
        self.rested = set(self.rocks)

    def spawn_sand(self, abyss = False):
        (x,y) = self.sand_source
        while True:
            if y >= self.abyss: break
            if (x, y + 1) not in self.rested:
                y += 1
                continue
            if (x - 1, y + 1) not in self.rested:
                x -= 1
                y += 1
                continue
            if (x + 1, y + 1) not in self.rested:
                x += 1
                y += 1
                continue
            break
        if abyss and y >= self.abyss:
            return False
        self.rested.add((x,y))
        if (x,y) == self.sand_source:
            return False
        return True



c = Cave(formations)
while True:
    res = c.spawn_sand(True)
    if not res:
        break
print("star1", len(c.rested) - len(c.rocks))
c = Cave(formations)
while True:
    res = c.spawn_sand()
    if not res:
        break
print("star2", len(c.rested) - len(c.rocks))
