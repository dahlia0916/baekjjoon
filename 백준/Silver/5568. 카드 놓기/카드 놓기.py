import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
card=[sys.stdin.readline().strip() for y in range(n)]
couple=[]
for h in range(n):
    if k==2:
        for j in range(n):
            if j!=h:
                couple.append(card[h]+card[j])
    elif k==3:
        for j in range(n):
            for g in range(n):
                if j != h and g != h and j!=g:
                    couple.append(card[h]+card[j]+card[g])
    else: 
        for j in range(n):
            for g in range(n):
                for t in range(n):
                    if j != h and g!=h and t!=h and (g != j and j!= t and g!=t) :
                        couple.append(card[h]+card[j]+card[g]+card[t])                
print(len(set(couple)))
