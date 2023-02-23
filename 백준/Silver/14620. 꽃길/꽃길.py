import sys
n=int(sys.stdin.readline())
l=[]
for i in range(n):
    l.append(list(map(int,sys.stdin.readline().strip().split())))
v=[[0]*n for _ in range(n)]
f=[[0]*n for _ in range(n)]
dy=[0,1,0,-1,0]
dx=[0,0,1,0,-1]
def check(y,x):
    for i in range(5):
        ny=y+dy[i]
        nx=x+dx[i]
        if v[ny][nx]==1:
            return True
    return False
def dfs(cnt):
    global sol,temp
    if cnt == 3:
        sol=min(sol,temp)
        return
    for i in range(1,n-1):
        for j in range(1,n-1):
            if check(i,j)==False:
                for k in range(5):
                    ny=i+dy[k]
                    nx=j+dx[k]
                    v[ny][nx]=1
                    temp=temp+l[ny][nx]
                dfs(cnt+1)
                for k in range(5):
                    ny=i+dy[k]
                    nx=j+dx[k]
                    v[ny][nx]=0
                    temp=temp-l[ny][nx]
sol=9999999999
temp=0
dfs(0)
print(sol)