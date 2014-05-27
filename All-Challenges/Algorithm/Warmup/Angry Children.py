# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
K = int(raw_input())
A = []
for i in range(N):
    A.append(int(raw_input()))

A.sort()
unfairness = A[K-1]-A[0]
for i in range(N-K):
   if unfairness > A[K+i-1]-A[i]:
    unfairness = A[K+i-1]-A[i]
    
print (unfairness)
