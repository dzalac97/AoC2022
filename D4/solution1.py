'''
Created Date: Sunday, December 4th 2022, 12:22:54 pm
Author: Domagoj Žalac
'''

def rangeSubset(range1, range2):
    return range1.start in range2 and range1[-1] in range2

def rangeOverlap(t1, t2):
    range1 = range(t1[0], t1[1] + 1)
    range2 = range(t2[0], t2[1] + 1)
    return rangeSubset(range1, range2) or rangeSubset(range2, range1)

with open('input', 'r') as file:
    cnt = 0
    for line in file:
        r1, r2 = line.strip().split(',')
        r1 = tuple(map(int, r1.split('-')))
        r2 = tuple(map(int, r2.split('-')))
        if rangeOverlap(r1, r2):
            cnt += 1
    print(cnt)
