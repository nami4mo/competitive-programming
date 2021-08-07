n,m=map(int, input().split())
gl=[[] for _ in range(n)]
degs=[0]*n
for _ in range(m):
    u,v=map(int, input().split())
    u-=1
    v-=1
    gl[u].append(v)
    degs[v]+=1

from collections import deque

q=deque()
for i in range(n):
    if degs[i]==0:q.append(i)

cnt=0
while q:
    for neib in gl[q.popleft()]:
        degs[neib]-=1
        if degs[neib]==0: q.append(neib)
    cnt+=1

if cnt==n:
    print('No')
else:
    print('Yes') 