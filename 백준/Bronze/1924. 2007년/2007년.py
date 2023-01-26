import sys
m,d = map(int,sys.stdin.readline().split())
sol=0
if m ==1 and d != 1:
    sol=(d-1)%7
elif m ==1 and d ==1:
    sol = 0
elif m ==2:
    sol=(31+d-1)%7
elif m == 3:
    sol = (31+28+d-1)%7
elif m == 4:
    sol = (31+28+31+d-1)%7
elif m == 5:
    sol = (31+28+31+30+d-1)%7
elif m == 6:
    sol = (31+28+31+30+31+d-1)%7
elif m == 7:
    sol = (31+28+31+30+31+30+d-1)%7
elif m == 8:
    sol = (31+28+31+30+31+30+31+d-1)%7
elif m == 9:
    sol = (31+28+31+30+31+30+31+31+d-1)%7
elif m == 10:
    sol = (31+28+31+30+31+30+31+31+30+d-1)%7
elif m == 11:
    sol = (31+28+31+30+31+30+31+31+30+31+d-1)%7
elif m == 12:
    sol = (31+28+31+30+31+30+31+31+30+31+30+d-1)%7

if sol == 0:
    print("MON")
elif sol == 1:
    print("TUE")
elif sol == 2:
    print("WED")
elif sol == 3:
    print("THU")
elif sol == 4:
    print("FRI")
elif sol == 5:
    print("SAT")
elif sol == 6:
    print("SUN")