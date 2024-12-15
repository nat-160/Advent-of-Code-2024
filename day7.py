#!/usr/bin/env python3

# load data
test_values = list()
operands = list()
with open("./data/7","r") as file:
    for line in file:
        t = line[:-1].split(": ")
        test_values.append(int(t[0]))
        operands.append([int(n) for n in t[1].split(" ")])

print(len(test_values), test_values[0])
print(len(operands), operands[0])

# pt 1
total = 0
for test_value, numbers in zip(test_values, operands):
    possible = set([numbers[0]])
    for number in numbers[1:]:
        t = set()
        for p in possible:
            t.add(p * number)
            t.add(p + number)
        possible = t
    if test_value in possible:
        total += test_value
print("Total:", total)

# pt 2
total = 0
for test_value, numbers in zip(test_values, operands):
    possible = set([numbers[0]])
    for number in numbers[1:]:
        t = set()
        for p in possible:
            t.add(p * number)
            t.add(p + number)
            t.add(int(str(p) + str(number)))
        possible = t
    if test_value in possible:
        total += test_value
print("Total:", total)