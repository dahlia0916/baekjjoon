import sys
n=int(sys.stdin.readline().strip())
deque=[]
for _ in range(n):
    inp=sys.stdin.readline().strip()
    if inp=="size" :
        print(len(deque))
    elif inp=="empty":
        if len(deque)==0:
            print(1)
        else:
            print(0)
    elif inp[0:3]=="pop":
        if len(deque)==0:
            print(-1)
        elif inp[4]=="f":
            print(deque[0])
            del deque[0]
        else:
            print(deque[-1])
            del deque[-1]
    elif inp[0:4]=="push":
        if inp[5]=="f":
            n=int(inp[11:])
            deque.insert(0,n)
        else:
            n=int(inp[10:])
            deque.append(n)
        
    elif inp=="front":
        if len(deque)==0:
            print(-1)
        else:
            print(deque[0])
    elif inp=="back":
        if len(deque)==0:
            print(-1)
        else:
            print(deque[-1])
    else:
        continue    