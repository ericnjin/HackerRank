# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
for i in range(n):
  s = raw_input()
  flag = 0
  code1 = []
  code2 = []
  code3 = []
  for j in s:
    if flag==0:
      if j==' ' or j=='-':
        flag = 1
      else:
      	code1.append(j)
    elif flag==1:
      if j==' ' or j=='-':
        flag = 2
      else:
      	code2.append(j)
    elif flag==2:
      	code3.append(j)
  print "CountryCode="+"".join(code1)+",LocalAreaCode="+"".join(code2)+",Number="+"".join(code3)    
