#!/usr/bin/env python3
import sys, string
a = string.ascii_letters
d = [x.strip() for x in sys.stdin.readlines()]
print("star1:{}".format(sum([a.index(list(set(l[:len(l)//2]) & set(l[len(l)//2:]))[0])+1 for l in d])))
print("star2:{}".format(sum([a.index(list(set.intersection(*map(set,d[i:i+3])))[0])+1 for i in range(0,len(d),3)])))

