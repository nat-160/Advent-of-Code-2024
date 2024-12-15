#!/usr/bin/env python3

# load data
disk_map = list()
with open("./data/9","r") as file:
    for line in file:
        for c in line[:-1]:
            disk_map.append(int(c))

n = len(disk_map)
disk = list()
for i in range(n):
    if i % 2: # i is odd
        for _ in range(disk_map[i]):
            disk.append(-1)
    else: # i is even
        for _ in range(disk_map[i]):
            disk.append(i // 2)
d = len(disk)
j = d - 1
for i in range(d):
    if disk[i] == -1:
        while disk[j] == -1:
            j -= 1
        if i >= j:
            break
        disk[i], disk[j] = disk[j], -1

checksum = 0
for i, block in enumerate(disk):
    if block == -1:
        break
    checksum += i * block

print(checksum)

disk = [([-1] * num if i % 2 else [i//2] * num) for i, num in enumerate(disk_map)]
print(disk)
d = len(disk)
for i in range(d - 1, -1, -2):
    for j in range(1, i, 2):
        if disk[j].count(-1) >= len(disk[i]):
            for k in range(len(disk[i])):
                disk[j][disk[j].index(-1)] = disk[i][k]
                disk[i][k] = -1
            break
print(disk)
dsk = list()
for d in disk:
    for n in d:
        dsk.append(n)
print(dsk)

checksum = 0
for i, block in enumerate(dsk):
    if block != -1:
        checksum += i * block

print(checksum)