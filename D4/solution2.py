'''
Created Date: Sunday, December 4th 2022, 4:04:08 pm
Author: Domagoj Žalac
'''

def rangeSubset(range1, range2):
    return set(range1).intersection(range2)

def rangeOverlap(t1, t2):
    range1 = range(t1[0], t1[1] + 1)
    range2 = range(t2[0], t2[1] + 1)
    return len(rangeSubset(range1, range2)) != 0

with open('input', 'r') as file:
    cnt = 0
    for line in file:
        r1, r2 = line.strip().split(',')
        r1 = tuple(map(int, r1.split('-')))
        r2 = tuple(map(int, r2.split('-')))
        if rangeOverlap(r1, r2):
            cnt += 1
    print(cnt)