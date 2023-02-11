import sys
S=sys.stdin.readline().strip('\n')
l=[]
for i in range(len(S)):
    l.append(S[i])
for i in range(len(l)):
    if l[i]==" ":
        continue
    elif 65<=ord(l[i])<=77:
        l[i]=chr(ord(l[i])+13)
    elif 78<=ord(l[i])<=90:
        l[i]=chr(ord(l[i])+13-26)
    elif 97<=ord(l[i])<=109:
        l[i]=chr(ord(l[i])+13)
    elif 110<=ord(l[i])<=122:
        l[i]=chr(ord(l[i])+13-26)
print(*l,sep="")