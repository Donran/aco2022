#!/usr/bin/env python3
import sys

data = sys.stdin.read().split("\n\n")

class Monkey:
    def __init__(self, monkey_data):
        self.homies = 1
        self.inspected_items_count = 0
        raw = [x.split(" ") for x in monkey_data.split("\n")[1:]]

        # Beautiful parsing, I know
        self.starting_items = [int(x[0].replace(",","")) for x in [a.split(", ") for a in raw[0][4:]]]
        self.items = self.starting_items.copy()

        (op, second) = raw[1][6:]
        if second == "old":
            self.operation = lambda x: x * x if op == "*" else x + x
        else:
            self.operation = lambda x: x * int(second) if op == "*" else x + int(second)
        self.prime = int(raw[2][-1])
        self.test = lambda x: x % self.prime == 0
        self.next = {
            True: int(raw[3][-1]),
            False: int(raw[4][-1])
        }

    def reset(self):
        self.inspected_items_count = 0
        self.items = self.starting_items

    def inspect_items(self, stressed=False):
        thrown_items = {}
        for el in self.items:
            el = self.operation(el)

            # Decrease worry level
            el %= self.homies
            if not stressed:
                el //= 3

            recipient = self.next[self.test(el)]

            if recipient not in thrown_items: thrown_items[recipient] = []
            thrown_items[recipient].append(el)

            self.items = self.items[1:]
            self.inspected_items_count += 1
        return thrown_items

    def catch_item(self, item):
        self.items.extend(item)


monkeys = []
tot = 1
for raw_monkey in data:
    m = Monkey(raw_monkey)
    monkeys.append(m)
    tot *= m.prime
for m in monkeys:
    m.homies = tot

for (star, rounds) in enumerate([20, 10000]):
    star += 1
    for i in range(rounds):
        for monkey in monkeys:
            thrown_items = monkey.inspect_items(stressed=True if star == 2 else False)
            for (monkey_idx, item) in thrown_items.items():
                monkeys[monkey_idx].catch_item(item)
    (first, second) = sorted([m.inspected_items_count for m in monkeys], reverse=True)[:2]
    print(f"Star {star}: {first*second}")
    for m in monkeys: m.reset()

