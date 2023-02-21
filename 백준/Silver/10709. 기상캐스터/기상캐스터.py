import sys
h,w = map(int,sys.stdin.readline().split())
for i in range(h):
    s=sys.stdin.readline().strip("\n")

    sol=[]
    ind=[]
    for j in range(w):
        if s[j] == 'c':
            ind.append(j)
    for ic in range(w):
        if s[ic]=='.':
            sol.append(-1)
        else:
            sol.append(0)
    for li in range(len(ind)-1):
        for li2 in range(1,ind[li+1]-ind[li]):
            sol[ind[li]+li2]=li2
    
    if len(ind)==1:
        for lt in range(ind[0]+1,w):
            sol[lt]=lt-ind[0]
    elif len(ind)>1:
        ind2=[]
        ind2.append(ind[-1])
        for lt3 in range(ind2[0]+1,w):
            sol[lt3]=lt3-ind2[0]
    print(*sol)
