import sys
n=int(sys.stdin.readline())
for i in range(n):
    N=int(sys.stdin.readline()) 
    c_t=0
    c_f=0
    j=2
    j2=5
    while j<=N:
        c_t=c_t+N//j
        j=j*2
    while j2<=N:
        c_f=c_f+N//j2
        j2=j2*5
    print(min(c_t,c_f))