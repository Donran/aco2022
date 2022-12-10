#!/usr/bin/env python3
import sys
data = [d.strip() for d in __import__("sys").stdin.readlines()]

class Sprite:
    def __init__(self):
        self.width = 3
    def visible(self, pos, pixel):
        mid = (self.width - 1)/2
        poses = [pos+x-mid for x in range(self.width)]
        return pixel in poses

class CRT:
    def __init__(self):
        self.width = 40
        self.height = 6

class CPU:
    def __init__(self):
        self.cycle = 0
        self.register = {
            'x': 1
        }
        self.crt = CRT()
        self.sprite = Sprite()
        self.signal_strength = 0
        self.scanlines = [""]

    def addx(self, *args):
        self.register['x'] += int(args[0])

    def noop(self): None

    def run(self, operations):
        for op in operations:
            self.do_operation(op)

    def do_operation(self, operation):
        ops = {
            'addx': {
                'cycles': 2,
                'function': self.addx
            },
            'noop': {
                'cycles': 1,
                'function': self.noop
            }
        }
        values = operation.split(" ")
        cmd = ops[values[0]]

        for _ in range(cmd['cycles']):
            scanline_idx = (self.cycle)//self.crt.width
            pixel_pos = (self.cycle) % (self.crt.width)

            # Signal strength (Star 1)
            if (self.cycle + 1 - 20) % 40 == 0:
                self.signal_strength += (self.cycle + 1) * self.register['x']

            # Draw scanlines (Star 2)
            isvis = self.sprite.visible(self.register['x'], pixel_pos)
            if not self.scanlines[scanline_idx]: self.scanlines.append("")
            self.scanlines[scanline_idx] += "#" if isvis else "."

            self.cycle += 1

        cmd['function'](*values[1:])

cpu = CPU()
cpu.run(data)

print(f"star1: {cpu.signal_strength}")
print("star2:")
for scanline in cpu.scanlines:
    for i in range(len(scanline)):
        if (i+1) % 5 != 0:
            print(scanline[i] if scanline[i] == "#" else " ", end="")
        else: print("\t", end="")
    print()
