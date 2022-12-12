'''
Created Date: Monday, December 12th 2022, 12:50:05 pm
Author: Domagoj Žalac
'''

import operator
import itertools as it
from math import prod

ops = { "*": operator.mul, "+": operator.add }

class Monkey:
    def __init__(self, items, operation, division):
        self._inspected = 0
        self._items = items
        self._operation = operation
        self._div = division[0]
        self._true = division[1]
        self._false = division[2]

    def _executeOperation(self, old):
        operator, value = self._operation[0], self._operation[1]
        if value == 'old':
            value = old
        return int(ops[operator](old, int(value)) / 3)

    def _testDivisibility(self, item, monkeys):
        if item % self._div == 0:
            monkeys[self._true]._items.append(item)
        else:
            monkeys[self._false]._items.append(item)

    def takeTurn(self, monkeys):
        while self._items:
            item = self._items.pop(0)
            item = self._executeOperation(item)
            self._testDivisibility(item, monkeys)
            self._inspected += 1
    
    def getInspectedItemsCount(self):
        return self._inspected

with open('input', 'r') as file:
    monkeys = []

    for key,group in it.groupby(file, lambda line: line.startswith('Monkey')):
        if not key:
            monkey = [line.strip() for line in group]
            items = [int(x) for x in monkey[0][len('Starting items: '):].split(',')]
            operation = monkey[1][len('Operation: new = old '):].split()
            div = int(monkey[2][len('Test: divisible by '):])
            true = int(monkey[3][len('If true: throw to monkey '):])
            false = int(monkey[4][len('If false: throw to monkey '):])
            division = [div, true, false]
            monkeys.append(Monkey(items, operation, division))

    for round in range(1, 21):
        for monkey in monkeys:
            monkey.takeTurn(monkeys)

    print('1st star:', prod(sorted([monkey.getInspectedItemsCount() for monkey in monkeys], reverse=True)[:2]))