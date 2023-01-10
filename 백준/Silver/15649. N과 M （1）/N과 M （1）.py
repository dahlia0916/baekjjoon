import sys
import itertools

n,m = map(int,sys.stdin.readline().split())
if m ==1:
    for i in range(1,n+1):
        print(i)
else:
    n_l=[]
    for i in range(1,n+1):
        n_l.append(i)
    for i in itertools.permutations(n_l,r=m):
        temp=str(i)
        temp=temp.strip("("")")
        temp=temp.replace(",","")
        print(temp)