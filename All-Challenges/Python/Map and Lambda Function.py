# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
A = []
for i in range(N):
    if i == 0:
      A.append(0)
    elif i == 1:
        A.append(1)
    else:
        A.append(A[i-1]+A[i-2])
cube = lambda a: a*a*a
print list(map(cube,A))
