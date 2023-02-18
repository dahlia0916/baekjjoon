import sys
a,b,c=map(int,sys.stdin.readline().split())

def go(a,b):
    if b == 1:
        return a%c
    else:
        temp=go(a,b//2)

        if (b%2==1):
            temp=(temp*temp*a)%c
        else:
            temp=(temp*temp)%c
        return temp
print(go(a,b))