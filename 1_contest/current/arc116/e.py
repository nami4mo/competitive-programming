from collections import deque
def make_order_parents(n,gl,root=0):
    order=[root]
    parents=[-1]*n
    q=deque([root])
    while q:
        poped=q.popleft()
        for neib in gl[poped]:
            if parents[neib]!=-1 or neib==root:continue
            parents[neib]=poped
            order.append(neib)
            q.append(neib)
    return order,parents


n,k=map(int, input().split())
gl=[[] for _ in range(n)]
for _ in range(n-1):
    u,v=map(int, input().split())
    u-=1
    v-=1
    gl[u].append(v)
    gl[v].append(u)

dists=[-1]*n
from collections import deque
q=deque([0])
dists[0]=0
start=-1
pares=[-1]*n
while q:
    poped=q.popleft()
    start=poped
    for neib in gl[poped]:
        if dists[neib]!=-1:continue
        dists[neib]=dists[poped]+1
        pares[neib]=poped
        q.append(neib)
# print(dists)

order,pare=make_order_parents(n,gl)
c_depth=[0]*n
for v in order[::-1]:
    # print(v)
    if pares[v]==-1:continue
    c_depth[pares[v]]=max(c_depth[v]+1, c_depth[pares[v]])

# print(c_depth)

ok, ng = n, 0
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    res = True
    # ...
    used=[False]*n
    
    
    if res: ok = mid
    else: ng = mid