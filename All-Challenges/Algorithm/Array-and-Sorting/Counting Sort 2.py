n = int(raw_input())

A = [0]*100
B = [int(x) for x in raw_input().split()]
for item in B:
    A[item] += 1
for i in range(len(A)):
    if A[i] != 0:
        for j in range(A[i]):
            print i,
    
