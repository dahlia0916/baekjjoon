import sys
n=int(sys.stdin.readline())
cnt=0
for i in range(n):
    l=[]
    s=sys.stdin.readline().strip()
    for l_l in range(len(s)):
        if len(l)==0:
            l.append(s[l_l])
        elif l[-1]==s[l_l]:
            l.pop()

        else:
            l.append(s[l_l])

    if len(l)==0:
        cnt=cnt+1
print(cnt)