#!/usr/bin/env python3

# load data
grid = list()
r, c = -1, -1
with open("./data/6","r") as file:
    row = 0
    for line in file:
        t = list()
        col = 0
        for cell in line[:-1]:
            if cell != "." and cell != "#":
                print(row,col)
                r, c = row, col
            t.append(cell)
            col += 1
        grid.append(t)
        row += 1
direction = ""
if grid[r][c] == "^":
    direction = "up"
if grid[r][c] == ">":
    direction = "right"
if grid[r][c] == "v":
    direction = "down"
if grid[r][c] == "<":
    direction == "left"
grid[r][c] = "X"
startR, startC, startD = r,c, direction
m = len(grid)
n = len(grid[0])
for row in range(m):
    print(grid[row])
print(direction, r,c)

# pt 1
while 0 <= r < m and 0 <= c < n:
    if direction == "up":
        if r - 1 < 0:
            break
        if grid[r-1][c] == "#":
            direction = "right"
        else:
            r -= 1
            grid[r][c] = "X"
    elif direction == "right":
        if c + 1 == n:
            break
        if grid[r][c+1] == "#":
            direction = "down"
        else:
            c += 1
            grid[r][c] = "X"
    elif direction == "down":
        if r + 1 == m:
            break
        if grid[r+1][c] == "#":
            direction = "left"
        else:
            r += 1
            grid[r][c] = "X"
    elif direction == "left":
        if c - 1 < 0:
            break
        if grid[r][c-1] == "#":
            direction = "up"
        else:
            c -= 1
            grid[r][c] = "X"
count = 0
for r in range(m):
    print(grid[r])
    for c in range(n):
        if grid[r][c] == "X":
            count += 1
print(count)

# pt 2
# brute force
count = 0
for row in range(m):
    for col in range(n):
        test = [[grid[r][c] for c in range(n)] for r in range(m)]
        if test[row][col] == "#":
            continue
        if row == startR and col == startC:
            continue
        test[row][col] = "#"
        r, c, direction = startR, startC, startD
        timer = 9999
        while timer > 0 and 0 <= r < m and 0 <= c < n:
            if direction == "up":
                if r - 1 < 0:
                    break
                if test[r-1][c] == "#":
                    direction = "right"
                else:
                    r -= 1
            elif direction == "right":
                if c + 1 == n:
                    break
                if test[r][c+1] == "#":
                    direction = "down"
                else:
                    c += 1
            elif direction == "down":
                if r + 1 == m:
                    break
                if test[r+1][c] == "#":
                    direction = "left"
                else:
                    r += 1
            elif direction == "left":
                if c - 1 < 0:
                    break
                if test[r][c-1] == "#":
                    direction = "up"
                else:
                    c -= 1
            timer -= 1
        if timer <= 0:
            count += 1
        print(count)
print(count)