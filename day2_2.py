import os, sys
"""if i%3 == 1 draw
if i%3 == 0 win
if i%3 == 2 lose
x = rock, 1 point for playing
y = paper, 2 points for playing
z = scissors, 3 points for playing"""

with open(os.path.join(sys.path[0], "day2"), "r") as f:
    data = f.readlines()

score = 0
for item in data:
    item.strip()
    item = item.split()
    if item[0] == "A":# steen
        if item[1] == "X":
            score += 0 + 3
        if item[1] == "Y":
            score += 3 + 1
        if item[1] == "Z":
            score += 6 + 2
    if item[0] == "B":# papier
        if item[1] == "X":
            score += 0 + 1
        if item[1] == "Y":
            score += 3 + 2
        if item[1] == "Z":
            score += 6 + 3
    if item[0] == "C":# schaar
        if item[1] == "X":
            score += 0 + 2
        if item[1] == "Y":
            score += 3 + 3
        if item[1] == "Z":
            score += 6 + 1
print(score)