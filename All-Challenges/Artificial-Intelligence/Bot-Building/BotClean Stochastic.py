#!/usr/bin/python
def distances(row,col,posr,posc):
  distance = []
  for i in range(len(row)):
    distance.append((row[i]-posr)**2+(col[i]-posc)**2)
  index = distance.index(min(distance))
  #print distance
  return [row[index],col[index]]
def next_move(posr, posc, board):
  if board[posr][posc] == 'd':
    board[posr][posc] = '-'
    print "CLEAN"
  else:
    row = []
    col = []
    for i in range(5):
      for j in range(5):
        if board[i][j] == 'd':
          row.append(i)
          col.append(j)
	#print row,col
    dpos = distances(row,col,posr,posc)
    #print dpos[0],posr,dpos[1],posc
    if dpos[0] < posr:
      print "UP"
    elif dpos[0]>posr:
      print "DOWN"
    elif dpos[1]<posc:
      print "LEFT"
    else:
      print "RIGHT"
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
