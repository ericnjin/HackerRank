import re
alpha = "qwertyuiopasdfghjklzxcvbnm0123456789"
n = int(raw_input())
tags = []
for i in range(n):
  s = raw_input()
  match = re.findall(r'<[^>]+>',s)
  for matches in match:
    tag = ""
    flag = 0
    if '</' not in matches:
      for j in matches:
        if j in alpha:
          tag += j
          flag = 1

        if (j == ' ' or j=='>') and flag == 1:
          break
      tags.append(tag)
tags = list(set(tags))
tags.sort()
print ";".join(tags)
