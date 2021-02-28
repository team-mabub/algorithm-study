import sys

num = sys.stdin.readline().rstrip()
original = int(num)

cnt = 0
while True:
    cnt += 1
    if len(num) == 1:
        num = num.zfill(2)
    back = num[1]
    sum_back = str(int(num[0]) + int(num[1]))[-1]
    new_num = back + sum_back
    if int(new_num) == original:
        break
    num = new_num

print(cnt)