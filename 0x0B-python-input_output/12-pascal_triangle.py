#!/usr/bin/python3
"""pascale_triangle module"""


def pascal_triangle(n):
    """a funct that returns a list of lists of integers
    representing the Pascal’s triangle"""
    if n <= 0:
        return []

    trngl = [[1]]
    while len(trngl) != n:
        prev_r = trngl[-1]
        new_r = [1]
        for x in range(len(prev_r) - 1):
            new_r.append(prev_r[x] + prev_r[x + 1])
        new_r.append(1)
        trngl.append(new_r)
    return trngl
