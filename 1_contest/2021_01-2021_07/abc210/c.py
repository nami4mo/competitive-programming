n,k=map(int, input().split())
cl=list(map(int, input().split()))
from collections import deque
q=deque()
d={}
l=0
cnt=0
ans=0

for c in cl:
    q.append(c)
    d.setdefault(c,0)
    d[c]+=1
    l+=1
    if d[c]==1:cnt+=1
    if l>k:
        p=q.popleft()
        d[p]-=1
        l-=1
        if d[p]==0:cnt-=1
    ans=max(cnt,ans)
print(ans)