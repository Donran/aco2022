#!/usr/bin/env python3
data = [x.strip() for x in __import__("sys").stdin.readlines()]


class Directory:
    def __init__(self, _name):
        self.name = _name
        self.subdirs = {}
        self.items = {}
    def add_item(self, _path, _name, value):
        if len(_path) > 0:
            self.subdirs[_path[0]].add_item(_path[1:], _name, value)
            return
        if value == 'dir':
            self.subdirs[_name] = Directory(_name)
        else:
            self.items[_name] = int(value)
    def get_size(self):
        total = sum(self.items.values())
        for (_,v) in self.subdirs.items():
            total +=  v.get_size()
        return total
    def get_subdirs(self):
        return self.subdirs.items()
    def pretty(self, indent = ""):
        print(f"{indent} {self.name} {self.get_size()}")
        indent += "\t"
        for v in self.subdirs.values():
            v.pretty(indent)
        for v in self.items.values():
            print(f"{indent} file {v}")


root = Directory('/')
path = []
for line in data:
    line = line.split(' ')
    if line[0] == '$':
        cmd = line[1]
        if cmd == 'cd':
            val = line[2]
            if val == '/':
                path = []
                continue
            elif val == '..':
                path.pop()
                continue
            path.append(val)
        continue
    (value, name) = line
    root.add_item(path, name, value)
def getsizes(d, fil):
    total = d.get_size()
    total = total if fil(total) else 0
    for (_,v) in d.get_subdirs():
        s = getsizes(v, fil)
        total += s
    return total
def getsmallest(d, free, required):
    s = d.get_size()
    smallest = 100000000000000000
    if free + s > required:
        smallest = s
    for (_, v) in d.get_subdirs():
        n = getsmallest(v, free, required)
        if n < smallest:
            smallest = n
    return smallest
    
#print(root.pretty())
free = 70000000 - root.get_size()
required = 30000000
print(getsizes(root, lambda x: x <= 100000))
print(getsmallest(root, free, required))
