import sys
n,m=map(int,sys.stdin.readline().split())
s_int={}
s_str={}
for i in range(n):
    inp=sys.stdin.readline().strip("\n")
    s_int[i+1]=inp
    s_str[inp]=i+1
for j in range(m):
    q=sys.stdin.readline().strip("\n")
    if q.isdigit()==True:
        print(s_int[int(q)])
    else:
        print(s_str[q])
    