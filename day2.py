#!/usr/bin/env python3

# load data
file = open("./data/2","r")
reports = list()
for line in file:
    temp = line.replace("\n","").split(" ")
    reports.append([int(x) for x in temp])

# pt 1
safe = 0
for report in reports:
    dir = report[1] - report[0]
    s = True
    for i in range(len(report)-1):
        diff = report[i+1] - report[i]
        if abs(diff) > 3 or dir * diff <= 0:
            s = False
            break
    safe += 1 if s else 0
print("Total Safe:", safe)

# pt 2
def subarr(arr):
    ret = list()
    ret.append(arr)
    for i in range(len(arr)):
        ret.append([arr[j] for j in range(len(arr)) if i!=j])
    return ret
safe = 0
for report in reports:
    for arr in subarr(report):
        dir = arr[1] - arr[0]
        s = True
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            if abs(diff) > 3 or dir * diff <= 0:
                s = False
                break
        if s:
            safe += 1
            break
print("w/ dampener:", safe)