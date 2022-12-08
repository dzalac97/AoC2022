'''
Created Date: Thursday, December 8th 2022, 3:10:59 pm
Author: Domagoj Žalac
'''

def checkLeftAndRightVisibility(treeMap, length, visibleTreeList, transposed):
    for row in range(1, length - 1):
        for col in range(1, length - 1):
            tree = treeMap[row][col]
            # left visibility
            key = (col, row) if transposed else (row, col)
            if key not in visibleTreeList and all(treeMap[row][i] < tree for i in range(col)):
                visibleTreeList.append(key)
            # right visibility
            if key not in visibleTreeList and all(treeMap[row][i] < tree for i in range(length - 1, col, -1)):
                visibleTreeList.append(key)

with open('input', 'r') as file:
    treeMap = [list(map(int, x.strip())) for x in file.readlines()]
    length = len(treeMap)
    visibleTreeList = []
    visibleTrees = 4 * length - 4
    checkLeftAndRightVisibility(treeMap, length, visibleTreeList, False)
    treeMapT = [list(x) for x in zip(*treeMap)]
    checkLeftAndRightVisibility(treeMapT, length, visibleTreeList, True)
    visibleTrees += len(visibleTreeList)
    print(visibleTrees)