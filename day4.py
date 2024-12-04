#!/usr/bin/env python3

# load data
file = open("./data/4","r")
grid = list()
for line in file:
    grid.append(list(line[:-1]))

# pt 1
count = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "X":
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if i | j and 0 <= r+i*3 < len(grid) and 0 <= c+j*3 < len(grid[0]):
                        if grid[r+i][c+j] + grid[r+2*i][c+2*j] + grid[r+3*i][c+3*j] == "MAS":
                            count += 1
print("XMAS:",count)

# pt 2
count = 0
valid = ["MS","SM"]
for r in range(1,len(grid)-1):
    for c in range(1,len(grid[0])-1):
        if grid[r][c] == "A":
            s1 = grid[r-1][c-1] + grid[r+1][c+1]
            s2 = grid[r-1][c+1] + grid[r+1][c-1]
            if s1 in valid and s2 in valid:
                count += 1
print("X-MAS:",count)