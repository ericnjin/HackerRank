for i in range(int(raw_input())):
    n = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    
    if a>b:
        [a,b] = (b,a)
    
    for j in range(n):
        print a*(n-1) + (b-a)*j,
        if a == b:
            break
    print 
