n = int(raw_input())
for i in range(n):
  a = raw_input()
  p1 = ""
  p2 = ""
  p3 = ""
  i = 0
  while i < len(a):
    if a[i].isalpha():
      p1 = p1+a[i]
      i = i+1
    else: 
      break
  while i < len(a):
    if a[i].isdigit():
      p2 = p2+a[i]
      i = i+1
    else: 
      break
  while i < len(a):
      p3 = p3+a[i]
      i = i+1
  if len(p1)<4 :
    if p1.islower() or len(p1)==0:
      if len(p2)<9 and len(p2)>1: 
        if len(p3)>=3:
          if p3[0].isupper() and p3[1].isupper() and p3[2].isupper:
    		print "VALID"
          else:
            print "INVALID"
        else:
            print "INVALID"
      else:
    		print "INVALID"
    else:
    		print "INVALID"      
  else:
    		print "INVALID"       
