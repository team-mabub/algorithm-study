test_cnt = int(input())

score = []
for i in range(test_cnt):
    parsing = input().split()
    temp = []
    for j in range(len(parsing)):
        temp.append(int(parsing[j]))
    score.append(temp)

for i in range(test_cnt):
    avg = sum(score[i][1:]) / float(score[i][0])
    cnt = len(list(filter(lambda x: x > avg, score[i][1:])))
    rate = cnt / float(score[i][0]) * 100
    print("{0:0.3f}%".format(rate))
