import sys   
len_a,len_b=map(int,sys.stdin.readline().split())
L_A=list(map(int,sys.stdin.readline().split()))
L_B=list(map(int,sys.stdin.readline().split()))
L_A.sort()
L_B.sort()

temp_in_b=0
sol=0
for i in range(len_a):
    while True:
        if L_A[i]<L_B[temp_in_b]:
            break
        elif L_A[i]==L_B[temp_in_b]:
            sol=sol+1
            break
        elif temp_in_b == len_b-1:
            if L_A[i]==L_B[temp_in_b]:
                sol=sol+1
                break
            else:
                break
        else:
            temp_in_b=temp_in_b+1
print(len_a+len_b-2*sol)