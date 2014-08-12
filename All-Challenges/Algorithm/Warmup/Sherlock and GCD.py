def GCD(a,b):
    if b == 0:
        return a;
    else:
        return GCD(b,a%b)
for _ in range(int(raw_input())):
    n = raw_input()
    A = [int(i) for i in raw_input().split()]
    gc = 0
    for i in A:
        gc = GCD(gc,i)
    if gc == 1:
        print 'YES'
    else:
        print 'NO'
