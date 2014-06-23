#!/bin/python
# Head ends here
def nextMove(n,r,c,grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                Pr = i
                Pc = j
    if Pr > r:
        return "DOWN"
    if Pr < r:
        return "UP"
    if Pc > c:
        return "RIGHT"
    if Pc < c:
        return "LEFT"
# Tail starts here
n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)
