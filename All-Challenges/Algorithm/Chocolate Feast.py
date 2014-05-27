T = int(raw_input())
for i in range(T):
    
    [N,C,M]=(int(i)  for i in raw_input().split())
    wrapper = N/C
    count = wrapper
    while(wrapper >= M):
        count = count + wrapper/M
        wrapper = wrapper%M + wrapper/M
    print count
    
