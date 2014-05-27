# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
for i in range(N):
    A = [x for x in raw_input().split()]
    if A[0] == "hackerrank" and A[-1] == "hackerrank":
        print 0
    elif A[0] == "hackerrank":
        print 1
    elif A[-1] == "hackerrank":
        print 2
    else:
        print -1
