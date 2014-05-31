#!/bin/python

# Head ends here
def insertionSort(a):    
    for i in range(len(a)):
        j = i
        while j>0 and a[j] < a[j-1]:
            [a[j],a[j-1]] = (a[j-1],a[j])
            j = j - 1
        if i > 0:    
         print  " ".join(str(i) for i in a[:])
                # Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
