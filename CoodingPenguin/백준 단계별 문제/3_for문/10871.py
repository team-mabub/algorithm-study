import sys

input_str_1 = sys.stdin.readline().split()
cnt = int(input_str_1[0])
limit = int(input_str_1[1])

num_list = []
input_str_2 = sys.stdin.readline().split()
for i in input_str_2:
    num_list.append(int(i))

result = []
for i in num_list:
    if i < limit:
        result.append(i)

for i in result:
    if result.index(i) == len(result) - 1:
        print(i)
    else:
        print(i, end=' ')