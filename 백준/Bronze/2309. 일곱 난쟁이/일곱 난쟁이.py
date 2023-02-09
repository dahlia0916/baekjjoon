import sys
s=[]
l=[]
for i in range(9):
    n=int(sys.stdin.readline())
    s.append(n)
ms=sum(s)-100
for i in range(9):
    for j in range(9):
        if i!=j and s[i]+s[j] == ms:
            l.append(s[i])
            l.append(s[j])

l=set(l)
if len(l)==2:
    s = [x for x in s if x not in list(l)]
else:
    l=list(l)
    l.sort
    temp=[]
    temp.append(l[0])
    temp.append(l[-1])
    s = [x for x in s if x not in temp]
s.sort()
for i in range(len(s)):
    print(s[i])