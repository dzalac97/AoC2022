'''
Created Date: Monday, December 11th 2022, 3:24:05 pm
Author: Domagoj Žalac
'''

with open('input', 'r') as file:
    lines = file.readlines()
    cmdLength = len(lines)
    cache, cycle, timer = 0, 0, 0
    X, sum = 1, 0
    crt = [list('.' * 40) for i in range(6)]
    while cycle < 240:
        cycle += 1
        timer -= 1
        if timer == 0:
            X += cache
            cache, timer = 0, 0
        if timer <= 0 and lines:
            cmd = lines.pop(0)
            if cmd.startswith('addx'):
                cache = int(cmd.split()[1])
                timer = 2
        if (cycle + 20) % 40 == 0 and cycle <= 220:
            sum += cycle * X
        row = cycle // 40
        col = cycle % 40 - 1
        if X - 1 <= col <= X + 1:
            crt[row][col] = '#'
    print('1st star:', sum)
    print('2nd star:')
    for row in crt:
        print(''.join(row))