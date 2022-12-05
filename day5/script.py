#!/usr/bin/env python3
import sys, queue
(towers, moves) = [data.split("\n")[:-1] for data in sys.stdin.read().split("\n\n")]
towers = [[tower[i] for i in range(1,len(tower), 4)] for tower in towers][::-1]
moves = [map(int, move.split(" ")[1::2]) for move in moves]
q = [[queue.LifoQueue() for _ in range(len(towers[0]))] for _ in range(2)]
for r in q:
    for t in towers:
        for (i, e) in enumerate(t): r[i].put(e) if e != ' ' else None
for (i,s,d) in moves:
    [q[0][d-1].put(q[0][s-1].get()) for _ in range(0,i)]
    [q[1][d-1].put(e) for e in [q[1][s-1].get() for _ in range(0,i)][::-1]]
print("\n".join(["Star {}: {}".format(i+1,"".join([x.queue[-1] for x in q[i]])) for i in range(len(q))]))
