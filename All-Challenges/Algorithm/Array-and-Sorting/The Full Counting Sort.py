import sys
N = int(raw_input())

store = ['']*100

for i in range(N):
    j,string = [x for x in raw_input().split()]
    if i<N/2:
        string = '-'
    store[int(j)] = store[int(j)] + string + ' '

for i in range(100):
           sys.stdout.write(store[i])
        
