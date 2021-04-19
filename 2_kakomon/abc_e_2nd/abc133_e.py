n,k=map(int, input().split())
MOD=10**9+7
gl=[[] for _ in range(n)]
for _ in range(n-1):
    u,v=map(int, input().split())
    u-=1
    v-=1
    gl[u].append(v)
    gl[v].append(u)

from collections import deque
q=deque([0])
visited=[False]*n
ans=k
while q:
    poped=q.popleft()
    visited[poped]=True
    cnt=0
    if poped==0: cnt=-1
    for neib in gl[poped]:
        if visited[neib]:continue
        ans*=(k-2-cnt)
        ans%=MOD
        cnt+=1
        q.append(neib)
print(ans)