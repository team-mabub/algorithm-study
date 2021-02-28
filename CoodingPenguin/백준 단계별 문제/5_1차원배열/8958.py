cnt = int(input())

score = []
for i in range(cnt):
    score.append(input())
    result = temp = 0
    for j in range(len(score[i])):
        if score[i][j] == 'O':
            temp += 1
            result += temp
        elif score[i][j] == 'X' and score[i][j-1] == 'O':
            temp = 0
    score[i] = result

for i in range(cnt):
    print(score[i])