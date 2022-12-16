#!/usr/bin/env python3
from functools import cmp_to_key
pairs = [[a.strip() for a in x.split("\n")] for x in open(0).read().split("\n\n")]

def walk(l, r):
    if isinstance(l, int):
        if isinstance(r, int):
            return r - l
        else:
            return walk([l], r)
    elif isinstance(r, int):
        return walk(l, [r])

    for i in range(len(l)):
        if i >= len(r): return -1
        res = walk(l[i], r[i])
        if res != 0:
            return res

    return len(r) - len(l)

star1 = 0
for (i, pair) in enumerate(pairs):
    if walk(eval(pair[0]), eval(pair[1])) >= 0:
        star1 += i+1
print("star1",star1)

pairs = [item for sublist in pairs for item in sublist][:-1]
pairs.append("[[2]]")
pairs.append("[[6]]")
pairs.sort(key=cmp_to_key(lambda a,b: walk(eval(a),eval(b))),reverse=True)
print("star2", (1 + pairs.index("[[2]]")) * (1 + pairs.index("[[6]]")))
