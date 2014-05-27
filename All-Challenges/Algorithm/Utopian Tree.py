# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
for i in range(n):
  N = int(raw_input())
  if N == 0:
    print 1
  else:
    if N%2 != 0:
      N = N/2 + 1
      print 2*(2**N-1)
    else:
      N = N/2
      print 2*(2**N-1)+1
