#!/usr/bin/env python3
import sys,copy
raw_rows = [x.strip() for x in sys.stdin.readlines()]
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def compare(self, other):
        return (self.x, self.y) == (other.x, other.y)
    def tuple(self): return (self.x, self.y)

class Node:
    def __init__(self, pos, elevation):
        self.elevation = elevation
        self.pos = pos
        self.valid_paths = []
    def add_path(self, pos, elevation):
        if elevation - self.elevation < -1: return False
        if (pos.x, pos.y) not in self.valid_paths:
            self.valid_paths.append((pos.x, pos.y))
        return True
class Map:
    def __init__(self, rows):
        # (y,x)
        self.map = []
        for (y, row) in enumerate(rows):
            new_row = []
            for (x, letter) in enumerate(row):
                if letter == "S":
                    letter = 'a'
                    self.start = Position(x,y)
                elif letter == "E":
                    letter = 'z'
                    self.end = Position(x,y)
                elevation = ord(letter) - ord('a')
                new_row.append(Node(Position(x,y), elevation))

            self.map.append(new_row)
        # Iterate paths
        for row in self.map:
            for node in row:
                self.update_paths(node.pos)
    def update_paths(self, start):
        for (y, x) in [(start.y + 1, start.x), (start.y - 1, start.x),(start.y, start.x + 1),(start.y, start.x -1)]:
            if y < 0 or y >= len(self.map): continue
            if x < 0 or x >= len(self.map[0]): continue
            cmp_el = self.map[y][x]
            self.map[start.y][start.x].add_path(cmp_el.pos, cmp_el.elevation)
        return False




    def print_map(self, win=None, ele=False):
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
                if win is not None and tmp_prev.tuple() in win and tmp_prev.tuple() in column.valid_paths and column.pos.tuple() in win: curr += "~"
                elif (tmp_prev.x, tmp_prev.y) in column.valid_paths:
                    curr += " "
                else: curr += "X"
                #curr += str(len(column.valid_paths))
                if column.pos.compare(self.start): curr += "S "
                elif column.pos.compare(self.end): curr += "E "
                elif win is not None and column.pos.tuple() in win: curr += "~~"
                else: curr += "  " if not ele else str(column.elevation).ljust(2)

                if win is not None and tmp_next.tuple() in win and tmp_next.tuple() in column.valid_paths: curr += "~"
                elif (tmp_next.x, tmp_next.y) in column.valid_paths:
                    curr += " "
                else: curr += "X"

                #print((tmp_below.x, tmp_below.y), column.valid_paths)

                if win is not None and tmp_below.tuple() in win and tmp_below.tuple() in column.valid_paths and column.pos.tuple() in win: below += "X~~X"
                elif (tmp_below.x, tmp_below.y) in column.valid_paths:
                    below += "X  X"
                else: below += "X"*4
                if win is not None and tmp_above.tuple() in win and tmp_above.tuple() in column.valid_paths and column.pos.tuple() in win: above += "X~~X"
                elif (tmp_above.x, tmp_above.y) in column.valid_paths:
                    above += "X  X"
                else: above += "X"*4
            print(above)
            print(curr)
            print(below)


m = Map(raw_rows)
m.print_map(None, False)

#def walk_map(current_pos, goal, branch = {}):
#    if goal.compare(current_pos): return (True, branch)
#    current_node = m.map[current_pos.y][current_pos.x]
#    branch[current_pos.tuple()] = {}
#    for walkable in current_node.valid_paths:
#        walkable_pos = Position(walkable[0], walkable[1])
#        print("Comparing", (walkable), (current_pos.y, current_pos.x))
#        been_here = False
#        for (k,_) in branch.items():
#            if k == walkable_pos.tuple(): been_here = True
#        if been_here: continue
#        (valid, rest) = walk_map(walkable_pos, goal, branch)
#        if valid:
#            branch[current_pos.tuple()][walkable_pos.tuple()] = rest
#    if len(branch[current_pos.tuple()].items()) != 0:
#        return (True, branch)
#    else:
#        return (False, {})
def test1():
    def walk_map(start, goal, branch = []):
        if start.pos.compare(goal.pos):
            return (True, branch)
        branches = []
        for walkable in start.valid_paths:
            #print(start.pos.tuple(), start.valid_paths, walkable)
            if walkable in branch: continue
            walkable_node = m.map[walkable[1]][walkable[0]]
            tmp_branch = copy.deepcopy(branch)
            tmp_branch.append(walkable_node.pos.tuple())
            (valid, new_branch) = walk_map(walkable_node, goal, tmp_branch)
            if valid:
                branches.append(new_branch)
        if len(branches) != 0:
            return (True, branches)
        else:
            start.valid_paths = []
            return (False, branches)
    shortest = 999999999999999999
    def do_the_thing_rekursion_ar_kul(fuck):
        global shortest
        for f in fuck:
            if isinstance(f[0], list):
                do_the_thing_rekursion_ar_kul(f)
            else:
                if len(f) < shortest: shortest = len(f)
    start_pos = m.map[m.start.y][m.start.x]
    end_pos = m.map[m.end.y][m.end.x]
    (win, paths) = walk_map(start_pos, end_pos)
    print(win)
    #print(paths)
    print(len(paths))
    do_the_thing_rekursion_ar_kul(paths)
    print(shortest)
def test2():
    
    def dijkstra(start):
        unvisited_nodes = [(x,y) for x in range(len(m.map[0])) for y in range(len(m.map))]
        shortest_path = {}
        previous_nodes = {}
        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        shortest_path[start] = 0
        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:
                if current_min_node == None or shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node
            if current_min_node == None: return
            el = m.map[current_min_node[1]][current_min_node[0]]
            for neighbour in el.valid_paths:
                tentative_value = shortest_path[current_min_node] + 1 #abs(el.elevation - m.map[neighbour[1]][neighbour[0]].elevation)
                if tentative_value < shortest_path[neighbour]:
                    shortest_path[neighbour] = tentative_value
                    previous_nodes[neighbour] = current_min_node
            unvisited_nodes.remove(current_min_node)
        return previous_nodes, shortest_path
    def print_result(previous_nodes, shortest_path, start_node, target_node):
        #print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
        path = []
        node = target_node
        while node != start_node:
            path.append(node)
            node = previous_nodes[node]

        #m.print_map(path)
        return list(reversed(path))

    # star 1
    #(previous_nodes, shortest_path) = dijkstra(m.start.tuple())
    #res = print_result(previous_nodes, shortest_path, m.start.tuple(), m.end.tuple())
    #print("star 1:", len(res))

    a_s = []
    for y in range(len(m.map)):
        for el in m.map[y]:
            if el.elevation == 0: a_s.append(el.pos.tuple())
    (previous_nodes, shortest_path) = dijkstra(m.end.tuple())
    shortest = sys.maxsize
    for a in a_s:
        try:
            res = print_result(previous_nodes, shortest_path, m.end.tuple(), a)
            if len(res) < shortest: shortest = len(res)
        except: continue
    print("star 2:", shortest)
test2()
