# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(raw_input())
for i in range(n):
  s = raw_input()
  match = re.search('^[\_\.]\d+[a-zA-Z]*\_?$',s)
  if match:
    print "VALID"
  else:
    print "INVALID"
