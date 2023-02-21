import sys
N,C = map(int,sys.stdin.readline().split())
l=list(sys.stdin.readline().split())
d={}
for i in range(len(l)):
    if l[i] in d:
        d[l[i]]=d[l[i]]+1
    else:
        d[l[i]]=1
d=sorted(d.items(), key=lambda x: x[1], reverse=True)

s=""
for i in range(len(d)):
    s=s+(str((d[i][0])+" ")*d[i][1])
print(s)