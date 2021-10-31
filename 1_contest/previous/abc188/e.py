n,m=map(int, input().split())
al=list(map(int, input().split()))
gl=[[] for _ in range(n)]
glr=[[] for _ in range(n)]
for _ in range(m):
    x,y=map(int, input().split())
    x-=1
    y-=1
    gl[x].append(y)
    glr[y].append(x)

INF=-10**18
maxl=[INF]*n
ail=[]
for i in range(n):
    ail.append((al[i],i))
ail.sort(key=lambda x: -x[0])
from collections import deque

ailq=deque(ail)
while ailq:
    val, start = ailq.popleft()
    if maxl[start] != INF:continue
    q=deque([start])
    while q:
        poped = q.popleft()
        for neib in glr[poped]:
            if maxl[neib]!=INF:continue
            maxl[neib]=val
            q.append(neib)

ans=-10**10
for i in range(n):
    buymax=maxl[i]
    gain=buymax-al[i]
    ans=max(ans,gain)
print(ans)
