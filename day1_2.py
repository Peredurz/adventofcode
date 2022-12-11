import os
import sys


lijst = []
getal = 0

with open(os.path.join(sys.path[0], "input"), "r") as file:
    for line in file:
        line = line.replace("\n", "")
        if line != "":
            getal += int(line)
        else:
            lijst.append(getal)
            getal = 0
totaal = 0
for i in range(0, 3):
    totaal += max(lijst)
    lijst.pop(lijst.index(max(lijst)))
    print(totaal)
