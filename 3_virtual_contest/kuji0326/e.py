n,k=map(int, input().split())
gl=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)

vis=[False]*n
from collections import deque
q=deque([0])
vis[0]=True

ans=k
MOD=10**9+7

while q:
    poped=q.popleft()
    cnt=0
    # print(poped)
    if poped==0:cnt=-1
    for neib in gl[poped]:
        if vis[neib]:continue
        ans*=(k-cnt-2)
        q.append(neib)
        vis[neib]=True
        cnt+=1
        ans%=MOD
print(ans)