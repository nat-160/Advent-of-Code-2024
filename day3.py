#!/usr/bin/env python3

# load data
file = open("./data/3","r")
instructions  = file.read()

# part 1
import re
queries = re.findall(r"mul\([0-9]+,[0-9]+\)", instructions)
total = 0
for capture in queries:
    num1 = int(capture[4:capture.index(",")])
    num2 = int(capture[capture.index(",")+1:-1])
    total += num1 * num2
print("Total", total)

# part 2
queries = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)", instructions)
total = 0
do = True
for capture in queries:
    if capture == "do()":
        do = True
    elif capture == "don't()":
        do = False
    elif do:
        num1 = int(capture[4:capture.index(",")])
        num2 = int(capture[capture.index(",")+1:-1])
        total += num1 * num2
print("Total", total)