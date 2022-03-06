import sys

while True:
    parsing = sys.stdin.readline().split()
    if len(parsing) != 2:
        exit()
    x, y = int(parsing[0]), int(parsing[1])
    print(x+y)