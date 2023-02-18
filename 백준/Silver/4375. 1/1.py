import sys
while(True):
    try:
        n=int(sys.stdin.readline())
    except:
        break
    s=1
    s_l=1
    while(True):
        if int(s)>=n and (int(s)%n)==0:
            print(s_l)
            break
        else:
            s=(s*10) + 1
            s_l=s_l+1