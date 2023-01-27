import sys
import math
n=int(sys.stdin.readline())
if n ==1:
    print(1)
elif n % 2 == 0:
    sol=2
    for i in range(1,(n//2)):#2가 1개부터 최대개수까지 쓰일때
        sol=sol+(math.factorial(i+(n-(i*2)))//(math.factorial(i)*math.factorial((n-(i*2)))))
    print(sol%10007)
else:
    sol=1
    for i in range(1,(n//2)+1):#2가 1개부터 최대개수까지 쓰일때
        sol=sol+(math.factorial(i+(n-(i*2)))//(math.factorial(i)*math.factorial((n-(i*2)))))
    print(sol%10007)