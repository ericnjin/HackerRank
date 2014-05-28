import re
n = int(raw_input())
for i in range(n):
  s = raw_input()
  if s[0] in "789":
    	
    	match = re.search(r"^\d\d\d\d\d\d\d\d\d\d$",s)

        if match:
          print "YES"
        else:
          print "NO"
  else:
      print "NO"
