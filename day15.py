#!/usr/bin/env python3

# load data
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename')
warehouse, movements, b = list(), list(), True
with open(parser.parse_args().filename, "r") as file:
    dir = {"^": "up", "v": "down", "<": "left", ">": "right"}
    for line in file:
        if len(line) == 1:
            b = False
        elif b:
            warehouse.append([c for c in line[:-1]])
        else:
            movements.extend([dir[c] for c in line[:-1]])


def locate(w):
    for r in range(len(w)):
        for c in range(len(w[0])):
            if w[r][c] == "@":
                return (r, c)


def v_search(w, r, c, dir):
    start, stop, step = (r-1, -1, -1) if dir == "up" else (r+1, len(w), 1)
    for i in range(start, stop, step):
        if w[i][c] == ".":
            return i
        elif w[i][c] == "#":
            return 0


def h_search(w, r, c, dir):
    start, stop, step = (c-1, -1, -1) if dir == "left" else (c+1, len(w[0]), 1)
    for i in range(start, stop, step):
        if w[r][i] == ".":
            return i
        elif w[r][i] == "#":
            return 0


def move(warehouse, movements):
    w = [[s for s in warehouse[i]] for i in range(len(warehouse))]
    r, c = locate(w)
    w[r][c] = "."
    for dir in movements:
        if dir == "up" or dir == "down":
            step = -1 if dir == "up" else 1
            v = v_search(w, r, c, dir)
            if v:
                for i in range(v, r, -step):
                    w[i][c] = w[i-step][c]
                r += step
        else:
            step = -1 if dir == "left" else 1
            h = h_search(w, r, c, dir)
            if h:
                for i in range(h, c, -step):
                    w[r][i] = w[r][i-step]
                c += step
    return w


def calculate(w):
    gps_sum = 0
    for r in range(len(w)):
        for c in range(len(w[0])):
            if w[r][c] == "O" or w[r][c] == "[":
                gps_sum += 100 * r + c
    return gps_sum


def expand(warehouse):
    w = list()
    convert = {"#": ["#", "#"], "O": ["[", "]"],
               ".": [".", "."], "@": ["@", "."]}
    for row in warehouse:
        new_row = list()
        for tile in row:
            new_row.extend(convert[tile])
        w.append(new_row)
    return w


def v_search_wide(w, r, c, dir):
    start, stop, step = (r-1, -1, -1) if dir == "up" else (r+1, len(w), 1)
    ret = list()
    search = set([c])
    for i in range(start, stop, step):
        next_search = set()
        for j in search:
            if w[i][j] == "#":
                return []
            elif w[i][j] == "[":
                next_search.update((j, j+1))
            elif w[i][j] == "]":
                next_search.update((j, j-1))
        if not next_search:
            break
        ret.append((i, next_search))
        search = next_search
    return ret


def move_wide(warehouse, movements):
    w = [[s for s in warehouse[i]] for i in range(len(warehouse))]
    r, c = locate(w)
    w[r][c] = "."
    for dir in movements:
        if dir == "up" or dir == "down":
            step = -1 if dir == "up" else 1
            v = v_search_wide(w, r, c, dir)
            if len(v) > 0:
                for row, cols in reversed(v):
                    for col in cols:
                        w[row+step][col] = w[row][col]
                        w[row][col] = "."
            if len(v) > 0 or w[r+step][c] == ".":
                r += step
        else:
            step = -1 if dir == "left" else 1
            h = h_search(w, r, c, dir)
            if h:
                for i in range(h, c, -step):
                    w[r][i] = w[r][i-step]
                c += step
    return w


warehouse_1 = move(warehouse, movements)
for w in warehouse_1:
    print("".join(w))
print(calculate(warehouse_1))

warehouse_2 = expand(warehouse)
warehouse_2 = move_wide(warehouse_2, movements)
for w in warehouse_2:
    print("".join(w))
print(calculate(warehouse_2))
