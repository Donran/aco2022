#!/usr/bin/env python3
data = [(i-65,j-88) for (i,j) in (map(ord,x.strip().split(" ")) for x in __import__("sys").stdin.readlines())]
print("star1:{}".format(sum([b+1+(1+b-a)%3*3 for (a,b) in data])))
print("star2:{}".format(sum([1+(a+(b-1))%3+b*3 for (a,b) in data])))
print(f"star1:{sum([1+(1+b-a)%3*3+b for (a,b) in data])}")
print(f"star2:{sum([1+(a+b-1)%3+b*3 for (a,b) in data])}")
