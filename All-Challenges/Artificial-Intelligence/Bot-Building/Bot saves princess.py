#!/bin/python
# Head ends here
def displayPathtoPrincess(n,grid):
#print all the moves here
# Tail starts here
      for i in range(n):
        for j in range(n):
           if grid[i][j] == 'p':
              Pr = i
              Pc = j
           elif grid[i][j] == 'm':
              r = i
              c = j
      move = ""
      if Pr > r:
         num_down = Pr - r
         for i in range(num_down):
             move = str(move) + "DOWN\n"
      if Pr < r:
         num_up = r - Pr
         for i in range(num_up):
             move = str(move) + "UP\n"
      if Pc > c:
         num_right = Pc - c
         for i in range(num_right):
             move = str(move) + "RIGHT\n"
      if Pc < c:
         num_left = c - Pc
         for i in range(num_left):
             move = str(move) + "LEFT\n"
      print move   

m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
