n = raw_input()
str = set(list(raw_input()))
for i in range(int(n)-1):
    b = raw_input()
    a = set(list(b))
    str = str.intersection(a)
print len(str)
