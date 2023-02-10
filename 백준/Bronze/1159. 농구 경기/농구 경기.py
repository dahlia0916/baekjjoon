import sys
n=int(sys.stdin.readline())
if n<5:
    print("PREDAJA")
else:
    l_l=""
    S={}
    l=[0]*n
    for i in range(n):
        inp=sys.stdin.readline()
        l[i]=(inp[0])
    for i in range(n):
        if l[i] not in S:
            S[l[i]]=1
        else:
            S[l[i]]=S[l[i]]+1
    l=list(set(l))
    for j in range(len(S)):
        if S.get(l[j])>=5:
            l_l=l_l+l[j]
    if l_l=="":
        print("PREDAJA" )
    else:
        temp=[]
        for i in range(len(l_l)):
            temp.append(l_l[i])
        temp.sort()
        print(*temp,sep="")
