import sys
sys.setrecursionlimit(10000)
def dfs(y,x):
    v[y][x]=1
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<N and 0<=nx<M and l[ny][nx]==1 and v[ny][nx]==0:
            dfs(ny,nx)

T=int(sys.stdin.readline())
for i in range(T):
    s=0
    M,N,K=map(int,sys.stdin.readline().split())
    l=[[0]*M for _ in range(N)]
    v=[[0]*M for _ in range(N)]
    for j in range(K):
        ipx,ipy=map(int,sys.stdin.readline().split())
        l[ipy][ipx]=1
    for i2 in range(N):
        for j2 in range(M):
            if l[i2][j2]==1 and v[i2][j2] == 0:
                dfs(i2,j2)
                s=s+1
    print(s)