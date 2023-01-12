import heapq
import sys
n = int(sys.stdin.readline())
data=[]
for i in range(n):
    s,e = map(int,sys.stdin.readline().split())
    data.append([s,e])
data.sort(key=lambda x:x[0])
cnt =1
h=[0]

for s,e in data:
    if s >= h[0]:
        heapq.heappop(h)
        heapq.heappush(h,e)
    else:
        cnt=cnt+1
        heapq.heappush(h,e)
print(cnt)