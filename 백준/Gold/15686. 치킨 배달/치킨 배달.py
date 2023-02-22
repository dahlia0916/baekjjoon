import sys
from itertools import combinations
n,m=map(int,sys.stdin.readline().split())
l=[]
for i in range(n):
    l.append(list(map(int,sys.stdin.readline().split())))
h_ind=[]
c_ind=[]
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            h_ind.append([i,j])
        elif l[i][j]==2:
            c_ind.append([i,j])
result = 999999
for chi in combinations(c_ind,m):
    sol=0
    for h in h_ind:
        s_h_len=999
        for ch in range(m):
            temp=abs(h[0]-chi[ch][0])+abs(h[1]-chi[ch][1])
            s_h_len=min(s_h_len,temp)
        sol=sol+s_h_len
    result=min(result,sol)
print(result)