n = int(raw_input())
A = [int(i) for i in raw_input().split()]

count  = 0

for j in range(1,n):
    value = A[j]
    i = j-1
    while i>=0 and A[i]>value:
        A[i+1] = A[i]
        i = i - 1
        count  += 1
        
    A[i+1] = value
print count
    
