import sys
n = int(sys.stdin.readline())
s=[list(map(int,input()))for _ in range(n)]
# for x in range(n):
#     s.append(sys.stdin.readline())
#     s[x]=s[x].strip()

def dfs(x,y,n):
    c=s[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if s[i][j] != c:
                c=-1
                break
    if c == -1:
        print("(",end="")
        n=n//2
        dfs(x,y,n)
        dfs(x,y+n,n)
        dfs(x+n,y,n)
        dfs(x+n,y+n,n)
        print(")",end="")
    elif c==1:
        print(1,end="")
    else:
        print(0,end="")

dfs(0,0,n)