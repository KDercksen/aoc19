#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input.txt") as f:
    lines = list(map(int, f.readlines()))

print(sum(line // 3 - 2 for line in lines))
