#!/usr/bin/env python3

# load data
file = open("./data/1","r")
l1, l2 = list(), list()
for line in file:
    temp = line.replace("\n","").split("   ")
    l1.append(int(temp[0]))
    l2.append(int(temp[1]))

# pt 1
s1, s2 = sorted(l1), sorted(l2)
dist = 0
for x, y in zip(s1, s2):
    dist += abs(x - y)
print("Total Distance:", dist)

# pt 2
from collections import Counter
scores = Counter(l2)
simil = 0
for x in l1:
    simil += x * scores[x]
print("Similarity Score:", simil)