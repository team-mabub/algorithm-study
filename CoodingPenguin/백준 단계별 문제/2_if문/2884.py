parsing = input().split()

hour = int(parsing[0])
minute = int(parsing[1])

if(minute - 45 < 0):
    minute = (60 + minute) - 45
    if(hour == 0):
        hour = 23
    else:
        hour -= 1
else:
    minute -= 45

print(str(hour) + " " + str(minute))