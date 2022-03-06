def result(tc):
    R = int(tc[0])
    S = tc[1]
    rt = ""

    for s in S:
        rt += s*R

    return rt

T = int(input())

for t in range(T):
    print(result(list(input().split())))