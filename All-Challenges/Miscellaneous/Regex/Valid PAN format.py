# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
num = '0123456789'
for i in range(N):
    A = raw_input()
    if len(A)==10:
       flag = 0 
       for i in range(5): 
        if A[i].isupper() != True:
            flag = 1
       for i in range(5,9): 
        if A[i] not in num: 
            flag = 1
       if A[9].isupper() == False:
            flag = 1
       if flag == 1:
                print "NO"
       else:
                    print "YES"
        
    else:
        print "NO"
