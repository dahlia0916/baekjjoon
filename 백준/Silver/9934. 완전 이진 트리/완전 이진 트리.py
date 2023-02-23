import sys
k=int(sys.stdin.readline())
l=list(map(str,sys.stdin.readline().strip().split()))
sol=[]
if len(l)%2 ==1:
    for K in range(k):
        temp=[]
        for i in range(len(l)):
            if i %2 ==0:
                temp.append(l[i])
        for j in range(len(temp)):
            l.remove(temp[j])
        sol.append(temp)
    for li in range(len(sol)-1,-1,-1):
        print(*sol[li])