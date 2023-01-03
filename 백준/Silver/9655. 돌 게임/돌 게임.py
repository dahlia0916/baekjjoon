import sys
s=["SK","CY"]
turn=0
n=int(sys.stdin.readline())
if n<=2:
    turn = n
else:
    while n>2:
        n=n-3
        turn=turn+1
    turn=turn+n

if turn %2 == 0:
    print(s[1])
else:
    print(s[0])
