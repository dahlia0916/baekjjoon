import sys
n=int(sys.stdin.readline())
for I in range(n):
    l=list(sys.stdin.readline().strip())
    stack=[]
    for i in range(len(l)):
        if len(stack)==0:
            stack.append(l[i])
        elif stack[-1]=="(":
            if l[i]==")":
                stack.pop()
            else:
                stack.append(l[i])
        
    if len(stack)==0:
        print("YES")
    else:
        print("NO")