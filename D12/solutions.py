'''
Created Date: Tuesday, December 13th 2022, 2:56:34 am
Author: Domagoj Žalac
'''

from collections import deque

def get2dIndex(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

def bfs(grid, start, reverse = False):
    queue = deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (not reverse and (x, y) == END) or (reverse and grid[x][y] == 'a'):
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < height and 0 <= y2 < width and (x2, y2) not in seen:
                diff = ord(grid[x2][y2]) - ord(grid[x][y])
                if (not reverse and diff <= 1) or (reverse and diff >= -1):
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))

with open('input', 'r') as file:
    lines = file.readlines()
    grid = [list(row.strip()) for row in lines]
    height = len(grid)
    width = len(grid[0])
    drawingBoard = [['.'] * width for i in range(height)]
    START = get2dIndex(grid, 'S')
    END = get2dIndex(grid, 'E')
    grid[START[0]][START[1]] = 'a'
    grid[END[0]][END[1]] = 'z'
    print('1st star:', len(bfs(grid, START)) - 1)
    print('2nd star:', len(bfs(grid, END, True)) - 1)

