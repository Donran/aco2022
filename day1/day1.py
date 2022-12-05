#!/usr/bin/env python3
data = "\n".join(list(map(lambda x: x.replace("\n", ""), open("day1.in").readlines())))
print("star1:{}".format(max([sum(int(i) for i in x.split("\n")) for x in data.split("\n\n")])))
print("star2:{}".format(sum(sorted([sum(int(i) for i in x.split("\n")) for x in data.split("\n\n")], reverse=True)[:3])))
