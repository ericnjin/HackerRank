import re
s = []
while(1):
  try:
    s.append(raw_input())
  except:
    break;
s = "\n".join(s)
match1 = re.search(r'import java.',s)
match2 = re.search(r'#include',s)

if match1:
  print "Java"
elif match2:
  print "C"
else:  
  print "Python"
  
