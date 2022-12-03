'''
Created Date: Saturday, December 3rd 2022, 5:27:06 pm
Author: Domagoj Žalac
'''

import sys
import string
from itertools import islice

GROUP_SIZE = 3

result = 0
with open('input', 'r') as file:
    for elfGroup in iter(lambda: list(islice(file, GROUP_SIZE)), []):
        elfGroupStripped = [rucksack.strip() for rucksack in elfGroup]
        commonItems = set.intersection(*map(set,elfGroupStripped))
        sum = 0
        for item in commonItems:
            sum += string.ascii_letters.index(item) + 1
        result += sum
print(result)