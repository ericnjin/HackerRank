n = int(raw_input())

A = [0]*100
B = [int(x) for x in raw_input().split()]
for item in B:
    A[item] += 1
for item in A:
    print item,
