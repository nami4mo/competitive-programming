a,n,m=map(int, input().split())
ll=[int(input()) for _ in range(n)]
left=ll[0]
right=ll[-1]
ds=[]
for i in range(n-1):
    d=ll[i+1]-ll[i]-1
    ds.append(d)

ds.sort()
from collections import deque
q=deque(ds)

xyl=[]
for i in range(m):
    x,y=map(int, input().split())
    d=x+y
    xyl.append((d,i,x,y))

xyl.sort(key=lambda x:x[0])

v=0
ansl=[0]*m
for d,i,x,y in xyl:
    while q and q[0]<=d:
        v+=q.popleft()
    ans=v+n+len(q)*d
    dl=min(left-1, x)
    dr=min(a-right, y)
    ans+=(dl+dr)
    ansl[i]=ans
for ans in ansl:print(ans)