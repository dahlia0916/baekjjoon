import sys
n=int(sys.stdin.readline())
for i in range(n):
    N=int(sys.stdin.readline())
    s={}
    for j in range(N):
        cloth,kind=sys.stdin.readline().split()
        if kind in s:
            s[kind]=s[kind]+1
        else:
            s[kind]=1
    r=1
    for k in s.keys():
        r=r*(s.get(k)+1)
    print(r-1)