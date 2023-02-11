import sys
n=int(sys.stdin.readline())
s=sys.stdin.readline().strip('\n')
f=""
l=""
for i in range(len(s)):
    if s[i]=="*":
        f=s[:i]
        l=s[i+1:]
for i in range(n):
    filen=sys.stdin.readline().strip('\n')
    if filen[:len(f)]==f:
        filen=filen[len(f):]
        if len(filen)<len(l):
            print("NE")
        else:
            if filen[-len(l):]==l:
                print("DA")
            else:
                print("NE")
    elif f+l == filen:
        print("DA")
    else:
        print("NE")