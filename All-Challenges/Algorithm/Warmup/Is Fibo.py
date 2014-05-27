fib = {}
f = [1, 1]
fib[1] = True
while f[-1] < 1e10:
    f.append(f[-1]+f[-2])
    fib[f[-1]] = True
T = input()
for i in xrange(T):
    N = input()
    if N in fib:
        print 'IsFibo'
    else:
        print 'IsNotFibo'
