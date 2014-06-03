#!/bin/python
def partition(ar):
    less = [x for x in ar if x<ar[0]]
    more = [x for x in ar if x>ar[0]]
    if len(ar) <= 1:
        
        return less+[ar[0]]+more
    pivot = ar[0]
    if len(less) > 0:
        less = partition(less)
    if len(more) > 0:
        more = partition(more)
        
    ar = less+[ar[0]]+more
    for item in ar:
        print item,
    print    
    return ar

def quickSort(ar):
    s = partition(ar)
m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)
