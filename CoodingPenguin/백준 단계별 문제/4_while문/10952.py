import sys

num = []
while True:
    parsing = sys.stdin.readline().split()
    x, y = int(parsing[0]), int(parsing[1])
    if x == 0 and y == 0:
        break
    else:
        num.append([x, y])

for i in range(len(num)):
    print(num[i][0] + num[i][1])