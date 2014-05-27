import re
n = raw_input()
tag = []
lib = {}
for i in range(int(n)):
    s = raw_input()
    match = re.findall(r'<\w[^>]*?>',s)
    for tags in match:
      j = ""
      for i in tags:
          if i == ' ' or i=='>':
            break
          else:
            j += i
      j = j[1:]
      if j not in tag:
        tag.append(j)
      
      rematch = re.findall(r'\w+\=[\"\']',tags)
      if len(rematch)==0:
		lib[j]=[]
      for attr in rematch:

          attr = attr[:-2]
      	  if j not in lib.keys():
             lib[j] = [attr]
          elif j in lib.keys() and attr not in lib[j]:
             lib[j].append(attr)
             lib[j] = list(set(lib[j]))
            
for key in sorted(lib.iterkeys()):
    lib[key].sort()
    print "%s:%s" % (key, ",".join(lib[key]))
