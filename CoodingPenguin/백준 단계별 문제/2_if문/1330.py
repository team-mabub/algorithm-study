inputstr = input().split()

num1 = int(inputstr[0])
num2 = int(inputstr[1])

if num1 > num2:
    print('>')
elif num1 == num2:
    print('==')
else:
    print('<')