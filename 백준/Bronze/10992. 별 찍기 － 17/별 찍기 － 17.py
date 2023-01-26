import sys
n=int(sys.stdin.readline())
if n ==1:
    print("*")
else:
    print((n-1)*" "+"*")
    for i in range(2,n):
        print((n-i)*" "+"*"+(2*(i-2)+1)*" "+"*")
    print((n-1)*"*"+"*"+(n-1)*"*")