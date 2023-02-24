import sys   
T=int(sys.stdin.readline())
for I in range(T):
    N=int(sys.stdin.readline())
    N_l=set(map(int,sys.stdin.readline().split()))
    M=int(sys.stdin.readline())
    M_l=list(map(int,sys.stdin.readline().split()))
    for i in M_l:
        if i in N_l:
            print(1)
        else:
            print(0)