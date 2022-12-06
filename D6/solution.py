'''
Created Date: Tuesday, December 6th 2022, 2:47:04 pm
Author: Domagoj Žalac
'''

with open('input', 'r') as file:
    signal = file.readline().strip()
    for i in range(len(signal) - 4):
        seq = signal[i : i + 4]
        if len(set(seq)) == 4:
            print('1st star:', i + 4)
            break
    for i in range(len(signal) - 14):
        seq = signal[i : i + 14]
        if len(set(seq)) == 14:
            print('2nd star:', i + 14)
            break