from typing import Deque


n=int(input())
xyl=[]
ma=-1
mi=10**10
for _ in range(n):
    x,y=map(int, input().split())
    if x>y:x,y=y,x
    xyl.append((x,y))
    ma=max(ma,x,y)
    mi=min(mi,x,y)

maa=10**10
mii=-1
for x,y in xyl:
    maa=min(maa,max(x,y))
    mii=max(mii,min(x,y))    
ans1=(ma-maa)*(mii-mi)

from collections import deque
xyl.sort()
q=deque(xyl)
bmin=xyl[0][0]
bmax=xyl[-1][0]

mindiff=bmax-bmin
swapped_min=10**10
while len(q)>=2:
    x,y=q.popleft()
    bmax=max(bmax,y)
    bmin=min(q[0][0],y,swapped_min)
    swapped_min=min(swapped_min,y)
    mindiff=min(mindiff,bmax-bmin)
    if swapped_min<=q[0][0]:break

xyl.sort(key=lambda x:x[1])
d=xyl[-1][1]-xyl[0][1]
mindiff=min(mindiff,d)
ans2=(ma-mi)*(mindiff)
ans=min(ans1,ans2)
print(ans)