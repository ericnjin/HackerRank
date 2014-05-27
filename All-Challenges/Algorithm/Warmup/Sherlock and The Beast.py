t = int(raw_input())
for i in range(t):
  
  n = int(raw_input())
  
  a = n/3
  b = n%3
  
  if b==0 :
    print "5"*n
  elif b == 2:
      a = a - 1
      b = 5
      if a>=0:
        s = "5"*a*3+"3"*b
        print s
      else:
        print "-1"
  elif b == 1:
      a = a - 3
      b = 10
      if a>=0:
        s = "5"*a*3+"3"*b
        print s  
      else:
        print "-1"
  else:
    print "-1"
