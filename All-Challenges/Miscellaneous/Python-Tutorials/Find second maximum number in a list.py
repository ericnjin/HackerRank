# Enter your code here. Read input from STDIN. Print output to STDOUT
n = raw_input()
m = [int(i) for i in raw_input().split()]
d = max(m)
while (d in m) == True:
    m.remove(max(m))
print max(m)
