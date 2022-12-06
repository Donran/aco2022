#!/usr/bin/env python3
d = __import__("sys").stdin.read()[:-1]

print("star1", list(filter(lambda x:x[1], [(i+4, len(set(d[i:i+4]))==4) for i in range(0,len(d))]))[0][0])
print("star2", list(filter(lambda x:x[1], [(i+14, len(set(d[i:i+14]))==14) for i in range(0,len(d))]))[0][0])
