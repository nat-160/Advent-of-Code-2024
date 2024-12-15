#!/usr/bin/env python3

# load data
topo = list()
with open("./data/10","r") as file:
    for line in file:
        topo.append([int(c) for c in line[:-1]])

m, n = len(topo), len(topo[0])

def trail(r, c, t):
    if topo[r][c] != t:
        return set()
    if t == 9:
        return set([(r,c)])
    ret = set()
    if r > 0:
        ret.update(trail(r - 1, c, t + 1))
    if r < m - 1:
        ret.update(trail(r + 1, c, t + 1))
    if c > 0:
        ret.update(trail(r, c - 1, t + 1))
    if c < m - 1:
        ret.update(trail(r, c + 1, t + 1))
    return ret
    
    
total = 0
for r in range(m):
    for c in range(n):
        if topo[r][c] == 0:
            t = trail(r, c, 0)
            total += len(t)
            #print(r, c, t)
print("Total:", total)

def trail(r, c, t):
    if topo[r][c] != t:
        return []
    if t == 9:
        return [[(r,c)]]
    ret = list()
    if r > 0:
        ret.extend(trail(r - 1, c, t + 1))
    if r < m - 1:
        ret.extend(trail(r + 1, c, t + 1))
    if c > 0:
        ret.extend(trail(r, c - 1, t + 1))
    if c < m - 1:
        ret.extend(trail(r, c + 1, t + 1))
    for i in range(len(ret)):
        ret[i].append((r,c))
    return ret

total = 0
for r in range(m):
    for c in range(n):
        if topo[r][c] == 0:
            t = trail(r, c, 0)
            total += len(t)
            print(r, c, t)
print("Total:", total)