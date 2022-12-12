#!/usr/bin/env python3
data = [[int(a) for a in x.strip()] for x in __import__("sys").stdin.readlines()]
count = len(data)*2 + (len(data[1:-1]))*2
for row in range(1, len(data)-1):
    for column in range(1, len(data[row])-1):
        max_top    = max([data[x][column] for x in range(0, row)])
        max_bottom = max([data[x][column] for x in range(row+1, len(data))])

        max_left   = max(data[row][:column])
        max_right  = max(data[row][column+1:])
        val = data[row][column]
        if val > max_left or val > max_right or val > max_top or val > max_bottom:
            count += 1
scenic = 0
for row in range(1, len(data)-1):
    for column in range(1, len(data[row])-1):
        curr = data[row][column]
        left, right, top, bot = (0,0,0,0)
        scenic_trees = []
        for tree in data[row][column-1::-1]:
            left += 1
            scenic_trees.append(tree)
            if tree >= curr: break
        for tree in data[row][column+1:]:
            right += 1
            scenic_trees.append(tree)
            if tree >= curr: break
        for tree in [data[x-1][column] for x in range(row, 0,-1)]:
            top += 1
            scenic_trees.append(tree)
            if tree >= curr: break
        for tree in [data[x][column] for x in range(row+1, len(data))]:
            bot += 1
            scenic_trees.append(tree)
            if tree >= curr: break
        scenic_value = left*right*top*bot
        scenic = scenic_value if scenic_value > scenic else scenic
        print(f"{data[row][column]}:{scenic_value}")
        print(scenic_trees, (top, left, right, bot))

print(f"star1: {count}")
print(f"star2: {scenic}")
