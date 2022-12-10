#!/usr/bin/env python3
import sys
data = [x.strip() for x in sys.stdin.readlines()]
moves = [[x for x in direction*int(times)] for (direction, times) in (d.split(" ") for d in data)]
moves = [item for sublist in moves for item in sublist]

class Position:
    def __init__(self):
        self.x = 0
        self.y = 0

class RopePart:
    def __init__(self, children=0):
        self.pos = Position()
        self.visited_positions = [(self.pos.x, self.pos.y)]
        if children != 0:
            self.child = RopePart(children-1)
        else:
            self.child = None

    def instruction(self, direction):
        if direction == "U": self.pos.y += 1
        elif direction == "D": self.pos.y -= 1
        elif direction == "L": self.pos.x -= 1
        elif direction == "R": self.pos.x += 1
        self.visited_positions.append((self.pos.x, self.pos.y))

    def move(self, parent_position):

        x_diff = parent_position.x - self.pos.x
        x_dir = 1 if parent_position.x > self.pos.x else -1

        y_diff = parent_position.y - self.pos.y
        y_dir = 1 if parent_position.y > self.pos.y else -1

        if abs(x_diff) > 1:
            self.pos.x += x_dir
            if abs(y_diff) == 1:
                self.pos.y += y_dir
        if abs(y_diff) > 1:
            self.pos.y += y_dir
            if abs(x_diff) == 1:
                self.pos.x += x_dir

        self.visited_positions.append((self.pos.x, self.pos.y))
        self.move_child()
    def get_unique_visits(self, children=False):
        res = [set(self.visited_positions)]
        if children and self.child is not None:
            res += self.child.get_unique_visits(children)
        return res

    def get_position(self, children=False):
        res = [(self.pos.x, self.pos.y)]
        if children and self.child is not None:
            res += self.child.get_position(children)
        return res

    def move_child(self):
        if self.child is not None:
            self.child.move(self.pos)

def print_large_map(positions):
    xes = [x[0] for x in positions]
    yes = [y[1] for y in positions]
    x_min = min(0, *xes)
    x_max = max(10, *xes)
    y_min = min(0, *yes)
    y_max = max(10, *yes)
    for row in range(x_min, x_max):
        for column in range(y_min, y_max):
            written = False
            for i in range(len(positions)):
                if (row+1, column+1) == positions[i]:
                    print(i if i != 0 else "H", end="")
                    written = True
                    break
            if written: continue
            if row-1 == 0 and column-1 == 0: print('s', end="")
            else: print(".", end="")
        print()

rope = RopePart(1)
for move in moves:
    rope.instruction(move)
    rope.move_child()
print(f"star 1: {len(rope.get_unique_visits(True)[1])}")

head = RopePart(9)
for move in moves:
    head.instruction(move)
    head.move_child()
print(f"star 2: {len(head.get_unique_visits(True)[9])}")
