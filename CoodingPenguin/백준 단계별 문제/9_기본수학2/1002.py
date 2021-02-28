from math import sqrt

N = int(input())
data = []
for i in range(N):
  data.append(list(map(int, input().split())))
for i in range(N):
  x1 = data[i][0]
  y1 = data[i][1]
  r1 = data[i][2]

  x2 = data[i][3]
  y2 = data[i][4]
  r2 = data[i][5]

  distance = sqrt((x2-x1)**2 + (y2-y1)**2)
  if x1 == x2 and y1 == y2:
    # 두 점이 같을 때 예외 처리
    if r1 == r2:
        # 무한대의 점 가능
        print(-1)
    else:
        # 불가능
        print(0)
  else:
    # 두 원은 서로 밖에 있으며 만나지 않는다
    if (r1 + r2) < distance:
      print(0)
    elif (r1 + r2) > distance and abs(r1 - r2) < distance:
      print(2)
    elif abs(r1 - r2) > distance:
      print(0)
    else:
      print(1)
            