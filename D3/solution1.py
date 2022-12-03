'''
Created Date: Saturday, December 3rd 2022, 4:58:54 pm
Author: Domagoj Žalac
'''

import sys
import string

file = open("input", "r")

result = 0
for line in file:
    rucksack = line.strip()
    compSize = int(len(rucksack)/2)
    comp1, comp2 =  rucksack[:compSize], rucksack[compSize:]
    commonChars = ''.join(set(comp1).intersection(comp2))
    sum = 0
    for commonChar in commonChars:
        sum += string.ascii_letters.index(commonChar) + 1
    result += sum
print(result)