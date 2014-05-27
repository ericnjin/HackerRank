#!/bin/python

# Complete the function below.


def  maxXor( l,  r):
   max1 = 0
   for i in range(l,r+1):
        for j in range(l,r+1):
            if max1 < i^j:
                max1 = i^j
            
   return max1
    

_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)

