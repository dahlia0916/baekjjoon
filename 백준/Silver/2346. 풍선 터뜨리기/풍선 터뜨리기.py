import sys
N=int(sys.stdin.readline().strip())
from collections import deque
deq=deque(map(int,sys.stdin.readline().split()))
ind=deque()
answer=[]
for j in range(N):
    ind.append(j+1)

for i in range(N):
    if len(deq)==1:
        answer.append(ind[0])
        break
    if i==0:
        move=deq[0]
    answer.append(ind[0])
    deq.popleft()
    ind.popleft()
    if move>0:
        deq.rotate(-(move-1))
        ind.rotate(-(move-1))
    else:
        deq.rotate(-(len(deq)+move))
        ind.rotate(-(len(deq)+move))
    move=deq[0]

print(*answer)
