'''
Created Date: Thursday, December 8th 2022, 6:16:16 pm
Author: Domagoj Žalac
'''

def checkLeftAndRightVisibility(treeMap, length, scenicScores, transposed):
    for row in range(1, length - 1):
        for col in range(1, length - 1):
            tree = treeMap[row][col]
            key = (col, row) if transposed else (row, col)
            # left visibility
            visible = True
            tmpCol = col - 1
            tmpScore = 1
            while visible and tmpCol > 0:
                visible = False
                if treeMap[row][tmpCol] < tree:
                    visible = True
                    tmpScore += 1
                tmpCol -= 1
            scenicScores[key[0]][key[1]] *= tmpScore
            # right visibility
            visible = True
            tmpCol = col + 1
            tmpScore = 1
            while visible and tmpCol < length - 1:
                visible = False
                if treeMap[row][tmpCol] < tree:
                    visible = True
                    tmpScore += 1
                tmpCol += 1
            scenicScores[key[0]][key[1]] *= tmpScore

with open('input', 'r') as file:
    treeMap = [list(map(int, x.strip())) for x in file.readlines()]
    length = len(treeMap)
    scenicScores = [[1] * length for i in range(length)]
    checkLeftAndRightVisibility(treeMap, length, scenicScores, False)
    treeMapT = [list(x) for x in zip(*treeMap)]
    checkLeftAndRightVisibility(treeMapT, length, scenicScores, True)
    print(max(map(max, scenicScores)))