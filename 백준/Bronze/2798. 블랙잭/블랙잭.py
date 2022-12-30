import sys
from itertools import combinations

data=[]
n,m= map(int,sys.stdin.readline().split())
data=(list(map(int,sys.stdin.readline().split())))
data.sort(reverse=True)
sol=[]
ans=[]
for i in combinations(data,3):
    sol.append(i)
for j in range(len(sol)):
    temp=sol[j][0]+sol[j][1]+sol[j][2]
    if temp<=m:
        ans.append(temp)
print(max(ans))