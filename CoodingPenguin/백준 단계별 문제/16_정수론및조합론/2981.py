import sys

input = sys.stdin.readline

import math

def solution(nums):
  diff = [x-y for x,y in zip(nums, nums[1:])]
  gcd = diff[0]
  for i in range(1, len(diff)):
    gcd = math.gcd(gcd, diff[i])
  
  result = list()
  for i in range(2, int(math.sqrt(gcd)+1)):
    if not gcd%i:
      result.extend([i, gcd//i])
  result.append(gcd)
  result = sorted(set(result))

  print(' '.join(map(str, result)))


if __name__ == "__main__":
  n = int(input())
  nums = list()
  for _ in range(n):
    nums.append(int(input()))
  solution(sorted(nums, reverse=True))