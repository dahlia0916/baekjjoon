import sys   
T=int(sys.stdin.readline())
for i in range(T):
    len_A,len_B=map(int,sys.stdin.readline().split())
    l_A=list(map(int,sys.stdin.readline().split()))
    l_B=list(map(int,sys.stdin.readline().split()))
    l_A.sort()
    l_B.sort()
    cnt=0
    sol=0
    for i in range(len_A):
        while True:
            if cnt == len_B or l_A[i]<=l_B[cnt]:
                sol=sol+cnt
                break
            else:
                cnt=cnt+1
    print(sol)