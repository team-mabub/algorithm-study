from collections import namedtuple

# 입력
n, k = map(int, input().split())
Stuff = namedtuple('Stuff', 'weight value')
lst = [Stuff(0, 0)]
for _ in range(n):
  w, v = map(int, input().split())
  stuff = Stuff(weight=w, value=v)
  lst.append(stuff)
lst.sort()


# 테이블 채우기
table = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
  w, v = lst[i].weight, lst[i].value
  for j in range(1, k+1):
    if w <= j:
      # 현재 물건을 넣었을 때의 최대값 vs 넣지 않았을 때의 최대값 비교
      if v + table[i-1][j-w] > table[i-1][j]:
        table[i][j] = v + table[i-1][j-w]
      else:
        table[i][j] = table[i-1][j]
    else:
      table[i][j] = table[i-1][j]

print(table[n][k])