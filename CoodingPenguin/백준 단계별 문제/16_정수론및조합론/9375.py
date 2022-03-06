import sys
from collections import Counter

input = sys.stdin.readline
t = int(input())
for _ in range(t):
  n = int(input())
  counter = Counter()
  for _ in range(n):
    _, cloth = input().rstrip().split()
    counter[cloth] += 1

  result = 1
  for item in counter:
    result *= (counter[item]+1)

  print(result-1)
