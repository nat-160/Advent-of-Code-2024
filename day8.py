#!/usr/bin/env python3

# load data
antennas = dict()
m, n = 0, 0
with open("./data/8","r") as file:
    for line in file:
        n = 0
        for cell in line[:-1]:
            if cell != ".":
                if cell not in antennas:
                    antennas[cell] = list()
                antennas[cell].append((m,n))
            n += 1
        m += 1

# pt 1
antinodes = set()
for a in antennas:
    for i in range(len(antennas[a])-1):
        for j in range(i+1, len(antennas[a])):
            r = antennas[a][i][0] - antennas[a][j][0]
            c = antennas[a][i][1] - antennas[a][j][1]
            row, col = antennas[a][i][0] + r, antennas[a][i][1] + c
            if 0 <= row < m and 0 <= col < n:
                antinodes.add((row, col))
            row, col = antennas[a][j][0] - r, antennas[a][j][1] - c
            if 0 <= row < m and 0 <= col < n:
                antinodes.add((row, col))
print("Node count:", len(antinodes))

# pt 2
antinodes = set()
for a in antennas:
    for i in range(len(antennas[a])-1):
        for j in range(i+1, len(antennas[a])):
            r = antennas[a][i][0] - antennas[a][j][0]
            c = antennas[a][i][1] - antennas[a][j][1]
            row, col = antennas[a][i][0], antennas[a][i][1]
            while 0 <= row < m and 0 <= col < n:
                antinodes.add((row, col))
                row, col = row + r, col + c
            row, col = antennas[a][j][0], antennas[a][j][1]
            while 0 <= row < m and 0 <= col < n:
                antinodes.add((row, col))
                row, col = row - r, col - c
print("Node count:", len(antinodes))