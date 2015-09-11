# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
dic = dict()
for j in range(N):
    a = [i for i in raw_input().split()]
    for i in range(1,len(a)):
        a[i] = float(a[i])+0.00
    dic[a[0]] = sum(a[1:])/len(a[1:])

c = round(dic[raw_input()],2)
if ((c - int(c))*100)%10 == 0:
    print str(c)+"0"
else:
    print c
