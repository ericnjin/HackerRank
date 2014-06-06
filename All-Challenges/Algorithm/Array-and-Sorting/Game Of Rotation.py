N = int(raw_input())
A = [int(x) for x in raw_input().strip().split()]
B = [int(x) for x in range(1,N+1)]

ws = sum((a*b for a,b in zip(A,B)))
total = sum(A)
maxi = ws

for i in range(N):
    ws = ws - total + A[i]*N
    
    if ws > maxi:
        maxi = ws
print maxi        
