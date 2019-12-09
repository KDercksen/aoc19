#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import deepcopy
from itertools import product

with open("input.txt") as f:
    opcodes_original = list(map(int, f.read().strip().split(",")))


for x, y in product(range(100), repeat=2):
    idx = 0
    opcodes = deepcopy(opcodes_original)
    opcodes[1:3] = [x, y]
    while (op := opcodes[idx]) != 99:
        fst, snd, target = opcodes[idx + 1 : idx + 4]
        if op == 1:
            opcodes[target] = opcodes[fst] + opcodes[snd]
            idx += 4
        elif op == 2:
            opcodes[target] = opcodes[fst] * opcodes[snd]
            idx += 4
    if opcodes[0] == 19690720:
        print(100 * opcodes[1] + opcodes[2])
