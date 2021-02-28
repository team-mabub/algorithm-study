num = []
for i in range(10):
    num.append(int(input()))

rest = []
for emt in num:
    rest.append(emt % 42)

rest = set(rest)
print(len(rest))