#!/usr/bin/env python3
data = [[r.split('-') for r in x.split(',')] for x in __import__("sys").stdin.read().split("\n")[:-1]]
groups = [[set([x for x in range(int(f)-1,int(s))]) for (f,s) in group] for group in data]
print("star1: {}".format(len([filter(lambda x:min(x)==0,[[len(a-b),len(b-a)] for (a,b) in groups])])))
print("star2: {}".format(len([filter(lambda x:len(x[0]&x[1]),groups)])))
