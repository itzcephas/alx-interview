#!/usr/bin/python3
"""
0. Pascal's Triangle
"""

def pascal_triangle(n):
    res = []

    for i in range(n):
        level = []
        C = 1

        for j in range(i + 1):
            level.append(C)
            C = C * (i - j) // (j + 1)

        res.append(level)

    return res

