# Enter your code here. Read input from STDIN. Print output to STDOUT.
import re
n = int(raw_input())
b = []
for i in range(n):
	b.extend(raw_input().split())

t = int(raw_input())
for i in range(t):
  count = 0
  c = raw_input()
  for j in range(len(b)):
    match = re.split(r'([^a-zA-Z0-9_\s])',b[j])
    
    count+=match.count(c)
  print count
