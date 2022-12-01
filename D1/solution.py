import sys

file = open("input", "r")
elves = [0]
elfIdx = 0
for line in file:
    val = line
    if val.strip():
        elves[elfIdx] += int(val)
    else:
        elves.append(0)
        elfIdx += 1
elves.sort(reverse=True)
print(sum(elves[:3]))