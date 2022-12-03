#!/usr/bin/env python3
a = __import__("string").ascii_letters
d = [x.strip() for x in __import__("sys").stdin.readlines()]
print("star1:{}".format(sum([a.index((set(l[:len(l)//2]) & set(l[len(l)//2:])).pop())+1 for l in d])))
print("star2:{}".format(sum([a.index((x&y&z).pop())+1 for(x,y,z)in(map(set,d[i:i+3])for i in range(0,len(d),3))])))

