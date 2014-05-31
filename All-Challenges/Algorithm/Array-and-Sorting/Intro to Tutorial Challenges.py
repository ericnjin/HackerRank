# Enter your code here. Read input from STDIN. Print output to STDOUT
f = int(raw_input())
r = int(raw_input())
a = [int(i) for i in raw_input().split()]
for i in range(len(a)):
    if f == a[i]:
        print i
        break
