import sys
n=int(sys.stdin.readline())
for i in range(n):
    t=int(sys.stdin.readline())
    if t <=2:
        print(t)
    elif t == 3:
        print(4)
    else:
        d=[0]*(t+1)#1 2 4 7 13
        d[1]=1
        d[2]=2
        d[3]=4
        for i in range(4,t+1):
            d[i]=d[i-1]+d[i-2]+d[i-3]
        print(d[t])