'''
Created Date: Friday, December 9th 2022, 2:22:12 pm
Author: Domagoj Žalac
'''
import numpy as np
from math import dist

def countTailPositions(lines, SNAKE_LENGTH):
    positions = {(0,0)}
    snake = [[0, 0] for x in range(SNAKE_LENGTH)]
    dirs = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}
    for line in lines:
        move, cnt = line.split()
        cnt = int(cnt)
        dir = dirs[move]
        while cnt > 0:
            snake[0][0] += dir[0]
            snake[0][1] += dir[1]
            for i in range(1, SNAKE_LENGTH):
                norm = dist(snake[i - 1], snake[i])
                if norm >= 2:
                    distance = [snake[i - 1][0] - snake[i][0], snake[i - 1][1] - snake[i][1]]
                    direction = [distance[0] / norm, distance[1] / norm]
                    direction = np.sign(direction) * np.ceil(np.abs(direction))
                    snake[i][0] += direction[0]
                    snake[i][1] += direction[1]
                    if i == SNAKE_LENGTH - 1:
                        positions.add(tuple(snake[i]))
            cnt -= 1
    return len(positions)

with open('input', 'r') as file:
    lines = file.readlines()
    print('1st star:', countTailPositions(lines, 2))
    print('2st star:', countTailPositions(lines, 10))