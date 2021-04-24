from heapq import heappush,heappop
from collections import deque

n,m=map(int, input().split())
hq=[]
xyl=[]
for _ in range(n):
    x,y=map(int, input().split())
    xyl.append((x,y))
al=[int(input()) for _ in range(m)]

al.sort()
xyl.sort(key=lambda x:x[0])
xyq=deque(xyl)

ans=0
for a in al:
    while xyq and xyq[0][0]<=a:
        poped=xyq.popleft()[1]
        heappush(hq,poped)
    while hq and hq[0]<a:
        heappop(hq)
    if hq:
        ans+=1
        heappop(hq)

print(ans)