#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input.txt") as f:
    wire1, wire2 = map(lambda x: x.strip().split(","), f.readlines())


def gen_locations(steps):
    locs = set()
    current = 0, 0
    for loc in steps:
        direction, num = loc[0], int(loc[1:])
        x, y = current
        if direction == "R":
            locs.update((x + i, y) for i in range(num + 1))
            current = x + num, y
        if direction == "L":
            locs.update((x - i, y) for i in range(num + 1))
            current = x - num, y
        if direction == "U":
            locs.update((x, y + i) for i in range(num + 1))
            current = x, y + num
        if direction == "D":
            locs.update((x, y - i) for i in range(num + 1))
            current = x, y - num
    return locs


crossings = gen_locations(wire1) & gen_locations(wire2)
best = sorted(crossings, key=lambda x: abs(x[0]) + abs(x[1]))[1]
print(abs(best[0]) + abs(best[1]))
