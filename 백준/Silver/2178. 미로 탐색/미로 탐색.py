import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
l=[]
for i in range(n):
    l.append(list(map(int,sys.stdin.readline().rstrip())))
dy=[1,0,-1,0]
dx=[0,1,0,-1]
def bfs(y,x):
    queue=deque()
    queue.append((y,x))
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and l[ny][nx]==1:
                queue.append((ny,nx))
                l[ny][nx]=l[y][x]+1
    return l[n-1][m-1]
print(bfs(0,0))