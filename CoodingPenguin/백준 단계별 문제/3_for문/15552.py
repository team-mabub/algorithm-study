import sys

test_cnt = int(sys.stdin.readline())

mem = []
for i in range(test_cnt):
    parsing = sys.stdin.readline().split()
    mem.append([int(parsing[0]), int(parsing[1])])

for i in range(test_cnt):
    print(mem[i][0] + mem[i][1])