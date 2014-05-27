# Enter your code here. Read input from STDIN. Print output to STDOUT
[n,m] = [int(i) for i in raw_input().split()]
count = 0
for i in range(m):
  [a,b,k]=[int(j) for j in raw_input().split()]
  count = count + (b - a + 1)*k
print count/n  
