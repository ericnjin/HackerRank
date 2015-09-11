# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(raw_input())
b = []
for i in range(n):
  b.append(raw_input())
b = " ".join(b)
t = int(raw_input())
c = []
for i in range(t):
  c = raw_input()
  d = c[:-2]+"se"
  match = re.findall("\s"+re.escape(c)+"\s",b)
  match2 = re.findall("\s"+re.escape(d)+"\s",b)
  print len(match)+len(match2)
