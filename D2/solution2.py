'''
Created Date: Friday, December 2nd 2022, 12:56:24 pm
Author: Domagoj Žalac
'''

import sys

def decode(line):
    d1, d2 = line.split()
    return p1[d1], p2[d2]

def calcWin(p1, outcome):
    if outcome == 3: # Draw
        return outcome + p1
    if outcome == 6: # Player 2 Wins
        return outcome + 1 + p1 % 3
    else: # Player 1 Wins
        return 3 + (p1 - 1) % -3

file = open("input", "r")

p1 = { 'A':1, 'B':2, 'C':3 }
p2 = { 'X':0, 'Y':3, 'Z':6 }
score = 0

for line in file:
    currP1, currOut = decode(line)
    score += calcWin(currP1, currOut)
print(score)