n,m=map(int, input().split())
gl=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)

ans=0
from collections import deque
for s in range(n):
    q=deque()
    q.append(s)
    vis=[False]*n
    vis[s]=True
    while q:
        poped=q.popleft()
        for neib in gl[poped]:
            if vis[neib]:continue
            vis[neib]=True
            q.append(neib)
    for i in range(n):
        if vis[i]:ans+=1
print(ans)