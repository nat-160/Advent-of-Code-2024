#!/usr/bin/env python3

# load data
plots = list()
with open("./data/12","r") as file:
    for line in file:
        plots.append([c for c in line[:-1]])
m, n = len(plots), len(plots[0])

visited = set()
def search(r,c,p):
    visited.add((r,c))
    ret = [(r,c)]
    for i in [-1,1]:
        if 0<=r+i<m and plots[r+i][c]==p and (r+i,c) not in visited:
            ret.extend(search(r+i,c,p))
        if 0<=c+i<n and plots[r][c+i]==p and (r,c+i) not in visited:
            ret.extend(search(r,c+i,p))
    return ret
    
def perimeter(region):
    p = 0
    for r, c in region:
        for i in [-1,1]:
            if not 0<=r+i<m or plots[r][c]!=plots[r+i][c]:
                p += 1
            if not 0<=c+i<n or plots[r][c]!=plots[r][c+i]:
                p += 1
    return p

def sides(region):
    s = 0
    region.sort()
    for i, cell in enumerate(region):
        r,c = cell
        for j in [-1,1]:
            if not 0<=r+j<m or plots[r][c]!=plots[r+j][c]:
                if i == 0 or region[i-1][0] != r or region[i-1][1] != c-1 or (0<=r+j<m and plots[r][c]==plots[r+j][c-1]):
                    s += 1
    region = sorted([(c,r) for r,c in region])
    for i, cell in enumerate(region):
        c,r = cell
        for j in [-1,1]:
            if not 0<=c+j<n or plots[r][c]!=plots[r][c+j]:
                if i == 0 or region[i-1][0] != c or region[i-1][1] != r-1 or (0<=c+j<n and plots[r][c]==plots[r-1][c+j]):
                    s += 1
    return s
            
price1 = price2 = 0
for r in range(m):
    for c in range(n):
        if (r,c) not in visited:
            t = search(r,c,plots[r][c])
            price1 += len(t) * perimeter(t)
            price2 += len(t) * sides(t)
print("Price 1:", price1)
print("Price 2:", price2)