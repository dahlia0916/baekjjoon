import sys
from collections import deque
n=int(sys.stdin.readline().strip())
n_deque=deque()
for i in range(n):
    n_deque.append(i+1)
while(len(n_deque)>2):
    n_deque.popleft()
    t=n_deque[0]
    n_deque.popleft()
    n_deque.insert(len(n_deque),t)
if len(n_deque)==1:
    print(n_deque[0])
else:
    print(n_deque[-1])