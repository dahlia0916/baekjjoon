import sys
n=int(sys.stdin.readline())
s=[]
for i in range(n):
    inp=int(sys.stdin.readline())
    s.append(inp)

s.sort()
for i in range(n):
    print(s[i])