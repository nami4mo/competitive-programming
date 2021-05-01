n,m,q=map(int, input().split())
gl=[[] for _ in range(n)]
for _ in range(m):
    a,b,c=map(int, input().split())
    a-=1
    b-=1
    gl[a].append((c,b))
    gl[b].append((c,a))

from heapq import heappop,heappush
ans=1
vis=[False]*n
vis[0]=1
q=[]
for c,v in gl[0]:
    heappush(q,(c,v))

xl=list(map(int, input().split()))
for x in xl:
    new_cvs=[]
    while q and q[0][0]<=x:
        _,v=heappop(q)
        if vis[v]:continue
        vis[v]=True
        ans+=1
        for cc,vv in gl[v]:
            new_cvs.append((cc,vv))
    print(ans)
    for cc,vv in new_cvs:heappush(q,(cc,vv))
