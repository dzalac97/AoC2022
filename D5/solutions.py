'''
Created Date: Monday, December 5th 2022, 2:52:13 pm
Author: Domagoj Žalac
'''

import re
import copy

crateStacks1 = []
crateStacks2 = []

with open('input', 'r') as file:
    
    for line in file:
        line = line.rstrip('\n')
        if line[1] == '1':
            break
        lineSize = len(line)
        for i in range(lineSize):
            if (i + 1) % 4 == 0:
                line = line[:i] + '|' + line[i+1:]
        line = line.replace('   ', '$')
        cols = line.split('|')
        if len(crateStacks1) == 0:
            crateStacks1 = [[] for x in range(len(cols))]
        for index, crate in enumerate(cols):
            if crate != '$':
                crateStacks1[index].append(crate)
    crateStacks2 = copy.deepcopy(crateStacks1)
    file.readline()

    for line in file:
        move = re.sub('\D', ' ', line.strip())
        cnt, frm, to = [int(x) for x in move.split()]
        for i in range(cnt):
            crateStacks1[to - 1].insert(0, (crateStacks1[frm - 1].pop(0)))
        for i in range(cnt, 0, -1):
            crateStacks2[to - 1].insert(0, (crateStacks2[frm - 1].pop(i - 1)))

    print('1st star: ' + ''.join([stack[0][1] for stack in crateStacks1]))
    print('2nd star: ' + ''.join([stack[0][1] for stack in crateStacks2]))