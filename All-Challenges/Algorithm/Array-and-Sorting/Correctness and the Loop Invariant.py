def insertion_sort(l):
    for i in xrange(1,len(l)):
        j = i-1
        while l[j]>l[j+1] and j>=0:
            [l[j],l[j+1]]=(l[j+1],l[j])
            j -= 1 
    print " ".join(map(str,l))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)