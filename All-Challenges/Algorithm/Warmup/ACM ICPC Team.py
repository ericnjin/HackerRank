n, m = [int(i) for i in raw_input().split()]
a = []
for _ in xrange(n):
    a.append(raw_input())

count = 0
MAX = 0

for i in xrange(n):
    for j in xrange(i+1,n):
        s = bin(int(str(a[i]),2) | int(str(a[j]),2))[2:]
        one_counts = s.count('1')
        if MAX < one_counts:
            MAX = one_counts
        if MAX == m:
            break
print MAX
for i in xrange(n):
    for j in xrange(i+1,n):
        s = bin(int(str(a[i]),2) | int(str(a[j]),2))[2:]
        one_counts = s.count('1')
        if MAX == one_counts:
            count += 1
print count
