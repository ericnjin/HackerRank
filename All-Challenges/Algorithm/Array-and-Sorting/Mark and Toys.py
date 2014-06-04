# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_toys(prices, rupees):
  #Compute and return final answer over here
  sigma = 0
  prices.sort()
  for i in range(len(prices)):
        sigma += prices[i]
        if sigma > rupees:
            i = i - 1
            break
  answer = i+1         
  return answer

if __name__ == '__main__':
  n, k = map(int, raw_input().split())
  prices = map(int, raw_input().split())
  print max_toys(prices, k)
