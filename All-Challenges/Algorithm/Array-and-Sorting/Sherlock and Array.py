for i in range(int(raw_input())):
    
    n = int(raw_input())
    A = [int(x) for x in raw_input().split()]
    
    total = sum(A)
    sigma = 0
    flag = -1
    
    for k in range(n):
      
        if total - sigma - A[k] == sigma:
            flag = 0
            break
            
        sigma += A[k] 
        
    if flag == 0:
            print "YES"
    else:
            print "NO"
