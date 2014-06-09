for i in range(int(raw_input())):
    P = [0,0]
    Q = [0,0]
    P[0],P[1],Q[0],Q[1] = [int(i) for i in raw_input().split()]
    print 2*Q[0]-P[0],2*Q[1]-P[1]
