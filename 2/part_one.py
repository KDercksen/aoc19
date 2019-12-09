#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input.txt") as f:
    opcodes = list(map(int, f.read().strip().split(",")))

idx = 0
while (op := opcodes[idx]) != 99:
    fst, snd, target = opcodes[idx + 1 : idx + 4]
    if op == 1:
        opcodes[target] = opcodes[fst] + opcodes[snd]
        idx += 4
    elif op == 2:
        opcodes[target] = opcodes[fst] * opcodes[snd]
        idx += 4

print(opcodes)
