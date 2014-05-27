# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
count = 0
for i in range(N):
    A = str(raw_input())
    A = A.lower()

    if "hackerrank" in A:
        count += 1
print count
