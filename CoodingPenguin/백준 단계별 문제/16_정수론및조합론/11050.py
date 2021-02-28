from functools import reduce

def result(n, k):
  if k == 0:
    return 1
  mult = lambda x,y:x*y
  return reduce(mult, range(n, n-k, -1))//reduce(mult, range(1, k+1))

n, k = map(int, input().split())
print(result(n, k))