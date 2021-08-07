import sys
input = sys.stdin.readline
n,m,x,y=map(int, input().split())
x-=1
y-=1
gl=[[] for _ in range(n)]
gli=[]
for i in range(m):
    a,b,t,k=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(i*2)
    gl[b].append(i*2+1)
    gli.append((a,b,t,k))
    gli.append((b,a,t,k))

from collections import deque
from heapq import heapify, heappop, heappush

q=[]
for gi in gl[x]:
    heappush(q,(0,gi))

INF=10**18
ds=[INF]*n
ds[x]=0
min_gi=[INF]*(m*2)
while q:
    # print(q)
    dist,gi=heappop(q)
    i,to,t,k=gli[gi]
    if i==y:break
    if min_gi[gi]<dist:continue
    if ds[to] <= dist+t:continue
    ds[to]=dist+t
    mint=ds[to]
    for gi2 in gl[to]:
        from2,to2,t2,k2=gli[gi2]
        rem=mint%k2
        if rem==0: min_k=mint
        else: min_k=mint+(k2-rem)
        if min_gi[gi2]<=min_k:continue
        min_gi[gi2]=min_k
        heappush(q,(min_k,gi2))

ans=ds[y]
if ans>=INF:
    ans=-1
print(ans)