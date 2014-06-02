#!/bin/python

# Head ends here
def insertionSort(ar):
    num = ar[-1]
    i= -2
    while num < ar[i]:
       ar[i+1] = ar[i]
       print " ".join(map(str, ar))
       i=i-1
       if ar[i+1] == ar[0]:
            break        
       

    ar[i+1] = num   
    print " ".join(map(str, ar))

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
