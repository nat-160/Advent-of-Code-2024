#!/usr/bin/env python3

# load data
positions, velocities = list(), list()
with open("./data/14","r") as file:
    for line in file:
        t = [x.split("=")[1].split(",") for x in line[:-1].split(" ")]
        positions.append((int(t[0][0]),int(t[0][1])))
        velocities.append((int(t[1][0]),int(t[1][1])))
n = len(positions)
width, height = 101, 103

def move(seconds):
    floor = [[0] * width for _ in range(height)]
    for robot in range(n):
        c, r = positions[robot]
        c += velocities[robot][0] * seconds
        r += velocities[robot][1] * seconds
        r %= height
        c %= width
        floor[r][c] += 1
    return floor

# pt 1
def quadrant(floor):
    quadrants = [0, 0, 0, 0, 0]
    for r in range(height):
        for c in range(width):
            if r == height//2 or c == width//2:
                0#quadrants[0] += floor[r][c]
            elif r < height//2:
                if c < width//2:
                    quadrants[1] += floor[r][c]
                else:
                    quadrants[2] += floor[r][c]
            elif c < width//2:
                quadrants[3] += floor[r][c]
            else:
                quadrants[4] += floor[r][c]
    return quadrants
    
# pt 1 ans
factor = 1
for q in quadrant(move(100))[1:]:
    factor *= q
print("Safety Factor:", factor)

# pt 2
def possibleTree(floor):
    for f in floor:
        best_consecutive, consecutive = 0, 0
        for n in f:
            if n == 0:
                consecutive = 0
            else:
                consecutive += 1
                best_consecutive = max(best_consecutive, consecutive)
        if best_consecutive > 7: # arbitrary number
            return True
    return False

# pt 2 ans
for i in range(9999999999):
    floor = move(i)
    if possibleTree(floor):
        for f in floor:
            print("".join([" " if n==0 else str(n) for n in f]))
        print("Possible Tree at", i)
        _ = input()