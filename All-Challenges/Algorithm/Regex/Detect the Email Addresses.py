# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(raw_input())
f = []
for i in range(n):
  s = " "+raw_input()+" "
  match = re.findall("[\w\.\S]+\@[\w\.\S]+\.\w\w\w?",s)
  for item in match:
      f.append(item)
f = list(set(f))  
f.sort()
print ";".join(f)
