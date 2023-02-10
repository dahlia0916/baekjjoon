import sys
a,b,c = map(int,sys.stdin.readline().split())
f_s,f_l=map(int,sys.stdin.readline().split())
s_s,s_l=map(int,sys.stdin.readline().split())
t_s,t_l=map(int,sys.stdin.readline().split())
l=[0]*(max(f_l,s_l,t_l)+1)
for i in range(f_s,f_l):
    l[i]=l[i]+1
for i in range(s_s,s_l):
    l[i]=l[i]+1
for i in range(t_s,t_l):
    l[i]=l[i]+1
s=0
for i in range(1,len(l)):
    if l[i]==1:
        s=s+a
    elif l[i]==2:
        s=s+2*b
    elif l[i]==3:
        s=s+3*c
print(s)