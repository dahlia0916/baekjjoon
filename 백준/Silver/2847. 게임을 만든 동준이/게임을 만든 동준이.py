import sys
n = int(sys.stdin.readline())
s=[]
sol=0
for i in range(n):
    m = int(sys.stdin.readline())
    s.append(m)
for j in range(n-1,0,-1):
    if s[j-1]>=(s[j]-1):
        sol=sol+(s[j-1]-(s[j]-1))
        s[j-1]=s[j-1]-(s[j-1]-(s[j]-1))

print(sol)