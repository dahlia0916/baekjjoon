import sys
S=sys.stdin.readline().strip()
alpa=[0]*26
for i in range(len(S)):
    alpa[ord(S[i])-97]=alpa[ord(S[i])-97]+1
print(*alpa)
