cnt = int(input())
num = []
parsing = input().split()
for i in range(cnt):
    num.append(int(parsing[i]))

num.sort()
print(str(num[0]) + ' ' + str(num[-1]))