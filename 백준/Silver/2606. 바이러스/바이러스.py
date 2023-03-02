import sys
n_c=int(sys.stdin.readline())
n=int(sys.stdin.readline())
data=[[] for I in range(n_c+1)]
v=[0]*(n_c+1)
for i in range(n):
    f,l=map(int,sys.stdin.readline().split())
    data[f]=data[f]+[l]
    data[l]=data[l]+[f]
def dfs(x):
    v[x]=1
    for nx in data[x]:
        if v[nx]==0:
            dfs(nx)
dfs(1)
print(sum(v)-1)