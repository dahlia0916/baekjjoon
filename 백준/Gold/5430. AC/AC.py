import sys
from collections import deque
t=int(sys.stdin.readline())
for i in range(t):
    ord=sys.stdin.readline().strip()
    n=int(sys.stdin.readline())
    data=sys.stdin.readline().strip()
    data=data[1:-1].split(",")
    queue = deque(data)

    r,f,b = 0,0,len(queue)-1
    flag=0

    if n==0:
        queue = []
        f=0
        b=0
    for j in range(len(ord)):
        if ord[j] == "R":
            r+=1
        elif ord[j] == "D":
            if len(queue) <1:
                f=1
                print("error")
                break
            else:
                if r%2==0:
                    queue.popleft()
                else:
                    queue.pop()

    if f==0:
        if r % 2 ==0:
            print('[' + ','.join(queue) + ']')
        else:
            queue.reverse()    
            print('[' + ','.join(queue) + ']')