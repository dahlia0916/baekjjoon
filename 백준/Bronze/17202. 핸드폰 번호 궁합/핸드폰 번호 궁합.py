n1 = list(map(int, input()))
n2 = list(map(int, input()))

A=[0 for x in range(16)]
for i in range(8):
    A[2*i]=n1[i]
    A[(2*i)+1]=n2[i]

while len(A)!=2:
    temp=[]
    for i in range(len(A)-1):
        s=(A[i]+A[i+1])%10
        temp.append(s)
    A=temp
sol=str(A[0])+str(A[1])
print(sol)