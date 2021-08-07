n,m,q=map(int, input().split())
wvl=[]
for _ in range(n):
    w,v=map(int, input().split())
    wvl.append((w,v))

wvl.sort()

xl=list(map(int, input().split()))

from collections import deque
from heapq import heappop, heappush

for _ in range(q):
    l,r=map(int, input().split())
    l-=1
    r-=1
    xll=[]
    for i in range(m):
        if l<=i<=r:continue
        xll.append(xl[i])
    xll.sort()
    vq=[]
    vdeq=deque(wvl)
    wi=0
    ans=0
    for x in xll:
        while vdeq and vdeq[0][0]<=x:
            w,v=vdeq.popleft()
            heappush(vq,-v)
        if vq:
            val=heappop(vq)
            ans+=(-1)*val
    print(ans)
