import sys
N=int(sys.stdin.readline())

for l in range(N):
    a=int(sys.stdin.readline())
    b=int(sys.stdin.readline())
    A=[]
    for k in range(b):
        A.append(k+1)
    for i in range(a):
        temp=[0 for x in range(b)]
        for j in range(b):
            if j==0:
                temp[0]=1
            else:
                temp[j]=A[j]+temp[j-1]
        A=temp
    print(A[b-1])