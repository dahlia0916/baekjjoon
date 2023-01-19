import sys
l=sys.stdin.readline()
l=l.strip()
sl=[]
sr=[]
for i in range(len(l)):
    sl.append(l[i])
n=int(sys.stdin.readline())
for cnt in range(n):
    inp=sys.stdin.readline()
    if inp[0] == "P":
        sl.append(inp[2])
        # print(sl)
    elif inp[0] == "L":
        if len(sl) != 0: 
            sr.append(sl.pop())
        # print(sl)
        # print(sr)
    elif inp[0] == "D":
        if len(sr) != 0:
            sl.append(sr.pop())
        # print(sl)
        # print(sr)
    elif inp[0] == "B":
        if len(sl) != 0:
            sl.pop()
        # print(sl)
        # print(sr)
for k in range(len(sl)):
    sr.append(sl.pop())
l_s=[]
for e in range(len(sr)):
    l_s.append(sr.pop())
print(*l_s,sep="")