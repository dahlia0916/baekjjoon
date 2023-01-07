import sys
n = int(sys.stdin.readline())
for z in range(n):

    s=0
    a,b,c = map(int,sys.stdin.readline().split())
    for i in range(1,a+1):
        for j in range(1,b+1):
            for l in range(1,c+1):
                if (i%j)==(j%l)==(l%i):
                    s=s+1
    print(s)