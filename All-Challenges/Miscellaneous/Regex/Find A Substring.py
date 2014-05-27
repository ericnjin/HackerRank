# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(raw_input())
s = []
for i in range(n):
  s.append(raw_input())

t = int(raw_input())  
s = " ".join(s)
for i in range(t):
  d = raw_input()
  match = re.findall(r'\w+'+re.escape(d)+'\w+',s)
  print len(match)
