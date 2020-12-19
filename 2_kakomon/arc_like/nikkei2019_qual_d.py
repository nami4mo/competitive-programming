
from collections import deque
n,m=map(int, input().split())
gl=[[] for _ in range(n)]
in_cnts=[0]*n
for _ in range(n+m-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    in_cnts[b]+=1

root = -1
for i in range(n):
    if in_cnts[i]==0:
        root=i
        break

ans=[-2]*n
ans[root]=-1
q=deque([root])
while q:
    node=q.popleft()
    for neib in gl[node]:
        in_cnts[neib]-=1
        if in_cnts[neib]==0:
            q.append(neib)
            ans[neib]=node

for a in ans:print(a+1)