# 입력
n = int(input())
operands = list(map(int, input().split()))
add, minus, mul, div = map(int, input().split())

# 최소/최대값 초기화
MIN = 1e10
MAX = -1e10

def dfs(i, now):
    global MIN, MAX, add, minus, mul, div

    # 모든 operands를 다 돌았을 경우
    # 연산이 완료됐으므로 현재값과 최소/최대값 비교 
    if i == n:
        MAX = max(MAX, now)
        MIN = min(MIN, now)
    # 다 돌지 않았을 경우
    # 즉 아직 연산할 게 남아있는 경우
    else:
        # 각 사칙연산에 맞춰 계산
        # 연산이 가능한 경우
        # 1. 연산을 소모했으므로 -1
        # 2. 그 다음 피연산자 위치와 계산 결과를 dfs로 넘김
        # 3. 2.가 끝났을 경우 다시 +1로 복구
        if add > 0:
            add -= 1
            dfs(i + 1, now + operands[i])
            add += 1
        if minus > 0:
            minus -= 1
            dfs(i + 1, now - operands[i])
            minus += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * operands[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / operands[i]))
            div += 1


dfs(1, operands[0])

print(MAX)
print(MIN)