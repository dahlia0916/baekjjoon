import sys
n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
l.sort(reverse=True)
A=[0 for x in range(n)]
# (5+0) (4+1) (4+2) (3+3)
for i in range(n):
    A[i]=l[i]+i
print(max(A)+1+1)