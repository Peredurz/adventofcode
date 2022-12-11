import os, sys

with open(os.path.join(sys.path[0], "day2"), "r") as f:
    data = f.readlines()
"""
A = rock
B = paper
C = scissors
x = rock, 1 point for playing
y = paper, 2 points for playing
z = scissors, 3 points for playing
if win, 6 points
if lose, 0 points
if draw, 3 points
first letter is what is played second is what you play, calculate score
"""
score = 0
for item in data:
    item.strip()
    item = item.split()
    if item[0] == "A" and item[1] == "X":
        score += 1 + 3
    elif item[0] == "A" and item[1] == "Y":
        score += 2 + 6
    elif item[0] == "A" and item[1] == "Z":
        score += 3 + 0
    elif item[0] == "B" and item[1] == "X":
        score += 1 + 0
    elif item[0] == "B" and item[1] == "Y":
        score += 2 + 3
    elif item[0] == "B" and item[1] == "Z":
        score += 3 + 6
    elif item[0] == "C" and item[1] == "X":
        score += 1 + 6
    elif item[0] == "C" and item[1] == "Y":
        score += 2 + 0
    elif item[0] == "C" and item[1] == "Z":
        score += 3 + 3
print(score)