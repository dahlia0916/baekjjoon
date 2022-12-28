import sys
data=[]
a,b,c,m = map(int,sys.stdin.readline().split())
if 24*a <= m:
    print(24*b)
elif a>m:
    print(0)
else:
    for i in range(24):
        if c>a:
            data.append(12*b)
        else:
            if ((((24-i)*a) - (i*c)) <= m):
                data.append((24-i)*b)
    print(max(data))