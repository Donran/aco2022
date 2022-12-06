#!/usr/bin/env python3
data = [d.split("\n") for d in __import__("sys").stdin.read().split("\n\n")[:-1]]
print(data)
print("star1:{}".format(max([sum(int(i) for i in x) for x in data])))
print("star2:{}".format(sum(sorted([sum(int(i) for i in x) for x in data], reverse=True)[:3])))
