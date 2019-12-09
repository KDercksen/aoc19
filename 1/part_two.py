#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("input.txt") as f:
    lines = list(map(int, f.readlines()))


print(
    sum(
        map(func := lambda fuel: 0 if (x := fuel // 3 - 2) <= 0 else x + func(x), lines)
    )
)
