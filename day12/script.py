#!/usr/bin/env python3
import sys,copy
raw_rows = [x.strip() for x in sys.stdin.readlines()]
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def compare(self, other):
        return (self.x, self.y) == (other.x, other.y)

class Node:
    def __init__(self, pos, elevation):
        self.elevation = elevation
        self.pos = pos
        self.valid_paths = []
    def add_path(self, pos, elevation):
        if (pos.x, pos.y) in self.valid_paths: return True
        if abs(self.elevation - elevation) <= 1:
            self.valid_paths.append((pos.x, pos.y))
            return True
        return False
class Map:
    def __init__(self, rows):
        # (y,x)
        self.map = []
        for (i, row) in enumerate(rows):
            new_row = []
            for (j, letter) in enumerate(row):
                if letter == "S":
                    letter = 'a'
                    self.start = Position(j,i)
                elif letter == "E":
                    letter = 'z'
                    self.end = Position(j,i)
                elevation = ord(letter) - ord('a')
                new_row.append(Node(Position(j,i), elevation))

            self.map.append(new_row)
        # Iterate paths
        for row in self.map:
            for node in row:
                self.update_paths(node.pos, Position(99999,9999))
    def update_paths(self, start, end):
        if start == end:
            return (True, [])
        for (j, i) in [(start.y + 1, start.x), (start.y - 1, start.x),(start.y, start.x + 1),(start.y, start.x -1)]:
            if j < 0 or j >= len(self.map): continue
            if i < 0 or i >= len(self.map[0]): continue
            cmp_el = self.map[j][i]
            self.map[start.y][start.x].add_path(cmp_el.pos, cmp_el.elevation)
        return False




    def print_map(self):
        for row in self.map:
            for column in row:
                print(str(column.elevation).ljust(3), end="")
            print()
        print()
        for row in self.map:
            for column in row:
                print(str(len(column.valid_paths)).ljust(3), end="")
            print()
        print()
        for row in self.map:
            below = ""
            above = ""
            curr = ""
            for column in row:
                tmp_next = copy.deepcopy(column.pos)
                tmp_next.x += 1
                tmp_prev = copy.deepcopy(column.pos)
                tmp_prev.x -= 1
                tmp_below = copy.deepcopy(column.pos)
                tmp_below.y += 1
                tmp_above = copy.deepcopy(column.pos)
                tmp_above.y -= 1
                #print(" ", end="")
                #print(len((column.valid_paths)), end="")
                #print((tmp_next.x, tmp_next.y), column.valid_paths)
                if (tmp_prev.x, tmp_prev.y) in column.valid_paths:
                    curr += " "
                else: curr += "X"
                #curr += str(len(column.valid_paths))
                if column.pos.compare(self.start): curr += "S "
                elif column.pos.compare(self.end): curr += "E "
                else: curr += "  "
                if (tmp_next.x, tmp_next.y) in column.valid_paths:
                    curr += " "
                else: curr += "X"
                #print((tmp_below.x, tmp_below.y), column.valid_paths)
                if (tmp_below.x, tmp_below.y) in column.valid_paths:
                    below += "X  X"
                else: below += "X"*4
                if (tmp_above.x, tmp_above.y) in column.valid_paths:
                    above += "X  X"
                else: above += "X"*4
            print(above)
            print(curr)
            print(below)


m = Map(raw_rows)
m.print_map()

#def walk_map(current_pos, prev_pos, goal, visited = []):
#    if goal.compare(current_pos): return (True, visited)
#    current_node = m.map[current_pos.y][current_pos.x]
#    walkables = []
#    for walkable in current_node.valid_paths:
#        walkable_pos = Position(walkable[0], walkable[1])
#        print("Comparing", (walkable), (current_pos.y, current_pos.x))
#        if prev_pos.compare(walkable_pos): continue
#        been_here = False
#        for v in visited:
#            if v.compare(walkable_pos): been_here = True
#        if been_here: continue
#        branch = copy.deepcopy(visited)
#        visited.append(walkable_pos)
#
#        (valid, rest) = walk_map(walkable_pos, current_pos, goal, visited)
#        if valid:
#            walkables.append(rest)
#    print(len(walkables))
#    branch = copy.deepcopy(walkables)
#    branch.append(visited)
#    return (len(walkables) != 0, branch)
def walk_map(current_pos, goal, branch = {}):
    if goal.compare(current_pos): return (True, branch)
    current_node = m.map[current_pos.y][current_pos.x]
    branch[current_pos] = {}
    for walkable in current_node.valid_paths:
        walkable_pos = Position(walkable[0], walkable[1])
        print("Comparing", (walkable), (current_pos.y, current_pos.x))
        been_here = False
        for (k,_) in branch.items():
            if k.compare(walkable_pos): been_here = True
        if been_here: continue

        (valid, rest) = walk_map(walkable_pos, goal, copy.deepcopy(branch[walkable_pos]))
        if valid:
            branch[current_pos][walkable_pos] = rest
    if len(branch[current_pos].items()) != 0:
        return (True, branch)
    else:
        return (False, {})

start_pos = m.map[m.start.y][m.start.x].pos
end_pos = m.map[m.end.y][m.end.x].pos
(win, paths) = walk_map(start_pos, end_pos)
print(win)
print(paths)
