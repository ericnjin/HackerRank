import re
n = int(raw_input())
for i in range(n):
  c = raw_input()
  match = re.findall(r'<a .+?</a>',c)
  for j in match:
    match2 = re.findall(r'href="(.+?)"',j)
    match3 = re.findall(r'>\s?([^>^<]+?)</',j)
    if len(match2) == 1 and len(match3) == 1:
    	print str(match2[0])+','+str(match3[0])
    if len(match3) == 0:
        print str(match2[0])+','
