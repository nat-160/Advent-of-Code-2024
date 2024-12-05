#!/usr/bin/env python3

# load data
file = open("./data/5","r")
rules = list()
update = list()
p = False
for line in file:
    if not p:
        rules.append(line[:-1].split("|"))
    else:
        update.append(line[:-1].split(","))
    if len(line) < 3:
        p = True

# pt 1
total = 0
for pages in update:
    valid = True
    for i in range(len(pages)-1):
        for j in range(i + 1, len(pages)):
            if [pages[i], pages[j]] not in rules:
                valid = False
                break
        if not valid:
            break
    if valid:
        total += int(pages[len(pages)//2])
print(total)

# pt 2
def fix(pages):
    bank = list(pages)
    ans = []
    while bank:
        left = bank.pop(0)
        valid = True
        for right in bank:
            if [left, right] not in rules:
                valid = False
        if valid:
            ans.append(left)
        else:
            bank.append(left)
    return ans

total = 0
for pages in update:
    valid = True
    for i in range(len(pages)-1):
        for j in range(i + 1, len(pages)):
            if [pages[i], pages[j]] not in rules:
                valid = False
                break
        if not valid:
            break
    if not valid:
        temp = fix(pages)
        total += int(temp[len(temp)//2])
print(total)