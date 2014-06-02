store = [0]*100
for i in range(int(raw_input())):
    n,s = [j for j in raw_input().split()]
    store[int(n)] += 1
sum = 0
for j in range(100):
    print store[j]+sum,
    sum += store[j]
