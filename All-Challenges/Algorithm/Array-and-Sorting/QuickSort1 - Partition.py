#!/bin/python

# Head ends here
def partition(ar): 
    less = [x for x in ar if x<ar[0]]
    more = [x for x in ar if x>ar[0]]
    return less+[ar[0]]+more

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
result = partition(ar)
for x in result:
    print x,
