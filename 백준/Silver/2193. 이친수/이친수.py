import sys
n = int(sys.stdin.readline())
if n <=2:
    print(1)
else:
    data=[0]*(n+1)
    data[1]=1
    data[2]=1
    for i in range(3,n+1):
        data[i]=data[i-1]+data[i-2]
    print(data[n])