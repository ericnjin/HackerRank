for i in range(int(raw_input())):
    M = int(raw_input())
    N = int(raw_input())
    A = [int(j) for j in raw_input().split()]
    
    B = map(lambda x:M - x,A)
    flag = 0
    
    for x in range(N):
        for y in range(x,N):
            if x == y:
                pass
            elif A[x] == B[y]:
                print x+1,y+1
                flag = 1
                break
        if flag == 1:
                    break
    
