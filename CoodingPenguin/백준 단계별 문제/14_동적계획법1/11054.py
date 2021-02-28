def fill(n, nums, table, reversed=False):
  for i in range(1, n):
    # 0부터 i까지의 부분 테이블 생성
    sub = [table[j] for j in range(0, i) if nums[j] < nums[i] ]
    if sub:
      # 있다면 서브 테이블의 최대값+1로 갱신
      table[i] = max(sub) + 1

  if reversed:
    # reversed라면 다시 역정렬해서 반환
    return table[::-1]
  return table


def result(n, nums):
  down_table, up_table = [0]*n, [0]*n

  # 정방향으로의 가장 긴 부분 수열
  down_table = fill(n, nums, down_table)
  # 역방향으로의 가장 긴 부분 수열
  up_table = fill(n, nums[::-1], up_table, reversed=True)

  sum_lr = [x+y for x, y in zip(down_table, up_table)]
  return max(sum_lr) + 1


n = int(input())
nums = list(map(int, input().split()))
print(result(n, nums))