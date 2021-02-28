import sys

cnt = int(sys.stdin.readline())

test_case = []
for i in range(cnt):
    parsing = sys.stdin.readline().split()
    test_case.append([int(parsing[0]), int(parsing[1])])

for i in range(cnt):
    print('Case #' + str(i+1) + ": " + str(test_case[i][0]) + ' + ' + str(test_case[i][1]) + ' = ' + str(test_case[i][0] + test_case[i][1]))