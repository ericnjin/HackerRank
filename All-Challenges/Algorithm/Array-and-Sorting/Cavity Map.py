import sys
n = input()
A = []
for _ in xrange(n):
    A += [list(i) for i in raw_input().split()]
for r in xrange(n):
    for c in xrange(n):
        if r == 0 or r == n-1 or c == 0 or c == n-1:
            pass
        else:
            if(A[r][c+1] < A[r][c] and A[r+1][c] < A[r][c] and A[r][c-1] < A[r][c] and A[r-1][c] < A[r][c]) == True:
                A[r][c] = 'X'
for r in xrange(n):
    for c in xrange(n):
        
            A[r][c] = str(A[r][c])
            
    print "".join(A[r])
 
