'''
Created Date: Friday, December 2nd 2022, 12:21:51 pm
Author: Domagoj Žalac
'''

def decode(line):
    d1, d2 = line.split()
    return p1[d1], p2[d2]

def calcWin(p1, p2):
    if (p1 % 3) + 1 == p2: # Player 2 Wins
        return p2 + 6
    if p1 == p2: # Draw
        return p2 + 3
    else: # Player 1 Wins
        return p2

file = open("input", "r")

p1 = { 'A':1, 'B':2, 'C':3 }
p2 = { 'X':1, 'Y':2, 'Z':3 }
score = 0

for line in file:
    currP1, currP2 = decode(line)
    score += calcWin(currP1, currP2)
print(score)