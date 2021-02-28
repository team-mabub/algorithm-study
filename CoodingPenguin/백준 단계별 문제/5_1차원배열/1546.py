cnt = int(input())

score = []
parsing = input().split()
for i in range(cnt):
    score.append(int(parsing[i]))

max_score = max(score)
total = 0.0
for i in range(cnt):
    score[i] = float(score[i]) / max_score * 100
    total += score[i]
print(total / len(score))