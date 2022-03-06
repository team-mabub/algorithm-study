test_cnt = int(input())

test_case = []
for i in range(test_cnt):
    parsing = input().split()
    test_case.append([int(parsing[0]), int(parsing[1])])

for i in range(test_cnt):
    print(test_case[i][0] + test_case[i][1])