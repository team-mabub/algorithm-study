import sys


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
table = [1] * (n)

for i in range(n):
  for j in range(i):
    if nums[j] < nums[i]:
        table[i] = max(table[i], table[j]+1)

print(max(table))