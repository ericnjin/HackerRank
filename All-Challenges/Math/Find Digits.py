for i in range(int(raw_input())):
    s = raw_input()
    lst = list(s)
    num = int(s)
    count = 0
    for item in lst:
        if item == '0':
            pass
        elif(num%int(item) == 0):
            count += 1
    print count    
