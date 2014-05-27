import re
n = int(raw_input())
b = []
for i in range(n):
  b.append(raw_input())
b = " ".join(b)
b = b + " "
t = int(raw_input())

for i in range(t):
  c = raw_input()
  d = c.replace("ou","o")
  k = re.compile(r'\b%s\b'%c,re.I)
  l = re.compile(r'\b%s\b'%d,re.I)
  
  match = k.findall(b)
  match2 = l.findall(b)
  print len(match)+len(match2)
