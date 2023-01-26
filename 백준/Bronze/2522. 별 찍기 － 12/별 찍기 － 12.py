import sys
n=int(sys.stdin.readline())

for i in range(1,n+1):
    print((n-i)*" "+i*"*")
for j in range(1,n+1):
    print(j*" "+(n-j)*"*")