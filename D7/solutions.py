'''
Created Date: Wednesday, December 7th 2022, 1:21:09 pm
Author: Domagoj Žalac
'''

import re

# Method iterates over terminal output and sums up file sizes for each directory separately
def calculateDirectoryFileSize(file, dirs):
    currPath = ''
    for line in file:
        output = line.strip()
        if output[0:4] == '$ ls':
            for line in file:
                if line[0] == '$':
                    output = line.strip()
                    break
                out1, out2 = line.split()
                if out1 != 'dir':
                    dirs[currPath] += int(out1)
        if output[0:4] == '$ cd':
            arg = output.split()[2]
            if arg == '..':
                currPath = re.sub('[^/]*/$', '', currPath)
            elif arg == '/':
                currPath = arg
            else:
                currPath += arg + '/'
            if currPath not in dirs:
                dirs[currPath] = 0

# Method iterates over directories and sums up total directory sizes starting from deepest paths
def calculateDirectorySize(dirs):
    sortedDirsByDepth = dict(sorted(dirs.items(), key=lambda item: item[0].count('/'), reverse=True))
    for path, size in sortedDirsByDepth.items():
        for tmpPath in sortedDirsByDepth:
            if path == tmpPath:
                continue
            if tmpPath in path:
                dirs[tmpPath] += size

with open('input', 'r') as file:
    dirs = {}

    calculateDirectoryFileSize(file, dirs)
    calculateDirectorySize(dirs)

    result1 = 0
    for path, size in dirs.items():
        if size <= 100000:
            result1 += size
    print('1st star:', result1)
    
    result2 = dirs['/']
    sortedDirsBySize = sorted(dirs, key=dirs.get, reverse=True)
    currentSpace = 70000000 - result2
    neededSpace = 30000000
    for key in sortedDirsBySize:
        dirSize = dirs[key]
        if currentSpace + dirSize < neededSpace:
            break
        result2 = dirs[key]
    print('2nd star:', result2)
