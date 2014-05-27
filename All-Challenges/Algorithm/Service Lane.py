[n,t] = [int(i) for i in raw_input().split()]
M = [int(j) for j in raw_input().split()]
for i in range(t):
    [a,b] = raw_input().split()
    print min(M[int(a):int(b)+1])  
