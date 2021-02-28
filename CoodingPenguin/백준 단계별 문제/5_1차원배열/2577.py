num = []
for i in range(3):
    num.append(int(input()))

result = num[0] * num[1] * num[2]
result = str(result)

cnt = [0] * 10
for i in range(len(result)):
    if result[i] == '0':
        cnt[0] += 1
    elif result[i] == '1':
        cnt[1] += 1
    elif result[i] == '2':
        cnt[2] += 1
    elif result[i] == '3':
        cnt[3] += 1
    elif result[i] == '4':
        cnt[4] += 1
    elif result[i] == '5':
        cnt[5] += 1
    elif result[i] == '6':
        cnt[6] += 1
    elif result[i] == '7':
        cnt[7] += 1
    elif result[i] == '8':
        cnt[8] += 1
    elif result[i] == '9':
        cnt[9] += 1

for i in cnt:
    print(i)