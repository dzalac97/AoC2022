'''
Created Date: Tuesday, December 6th 2022, 2:47:04 pm
Author: Domagoj Žalac
'''

def findStartOfMarker(signal, distNum):
    for i in range(len(signal) - distNum):
        seq = signal[i : i + distNum]
        if len(set(seq)) == distNum:
            return i + distNum

with open('input', 'r') as file:
    signal = file.readline().strip()
    print('1st star:', findStartOfMarker(signal, 4))
    print('2nd star:', findStartOfMarker(signal, 14))