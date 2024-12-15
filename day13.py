#!/usr/bin/env python3

# load data
from sympy import *
matrices = list()
with open("./data/13","r") as file:
    matrix = list()
    for line in file:
        t = line.split(" ")
        if "A" in line:
            matrix = [[0] * 3 for _ in range(2)]
            matrix[0][0] = int(t[2][2:-1])
            matrix[1][0] = int(t[3][2:-1])
        elif "B" in line:
            matrix[0][1] = int(t[2][2:-1])
            matrix[1][1] = int(t[3][2:-1])
        elif "Prize" in line:
            matrix[0][2] = int(t[1][2:-1])
            matrix[1][2] = int(t[2][2:-1])
            matrices.append(matrix)

def calc(matrix):
    m = Matrix(matrix).rref()[0]
    if m[2].is_integer and m[5].is_integer:
        return 3 * m[2] + m[5]
    return 0

def calc10000000000000(matrix):
    matrix[0][2] += 10000000000000
    matrix[1][2] += 10000000000000
    m = Matrix(matrix).rref()[0]
    if m[2].is_integer and m[5].is_integer:
        return 3 * m[2] + m[5]
    return 0

tokens = tokens2 = 0
for matrix in matrices:
    tokens += calc(matrix)
    tokens2 += calc10000000000000(matrix)
print("Tokens:", tokens)
print("Tokens:", tokens2)