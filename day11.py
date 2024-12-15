#!/usr/bin/env python3

# load data
from collections import Counter
stones = Counter()
with open("./data/11","r") as file:
    for s in [int(s) for s in file.read()[:-1].split(" ")]:
        stones[s] += 1

for _ in range(75):
    n_stones = Counter()
    for stone, i in stones.items():
        if stone == 0:
            n_stones[1] += i
        elif len(str(stone))%2==0:
            t = str(stone)
            n_stones[int(t[:len(t)//2])] += i
            n_stones[int(t[len(t)//2:])] += i
        else:
            n_stones[2024 * stone] += i
    stones = n_stones
print(stones)
print(sum(stones.values()))