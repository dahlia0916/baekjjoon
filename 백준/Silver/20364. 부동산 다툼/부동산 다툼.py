import sys

n, q = map(int, sys.stdin.readline().split())
visited = [0] * (n + 1)

for i in range(q):
    tan = int(sys.stdin.readline())
    target = tan
    flag = 0 
    while target != 1:
        if visited[target] >= 1:
            flag = target 

        target //= 2
    if flag:
        print(flag)
    else:
        visited[tan] = 1
        print(0)
        