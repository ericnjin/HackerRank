# Enter your code here. Read input from STDIN. Print output to STDOUT
A = raw_input()
x = raw_input()

count = 0
for i in range(len(A)-len(x)):
     
    if A[i:i+len(x)] == x:
        count += 1
print count
