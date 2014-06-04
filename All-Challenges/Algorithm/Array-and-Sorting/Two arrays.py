for i in range(int(raw_input())):
    n,k = [int(x) for x in raw_input().split()]
    a = [int(x) for x in raw_input().split()]
    b = [int(x) for x in raw_input().split()]
    
    a.sort()
    b.sort(reverse=True)
    
    s = [sum(x) for x in zip(a,b)]
    k_bar = min(s)
    
    if k_bar < k:
        print "NO"
    else:
        print "YES"
