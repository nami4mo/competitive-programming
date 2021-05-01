from heapq import heappop,heappush

n,m,q=map(int,input().split())
gl=[[] for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    gl[a-1].append((c,b-1))
    gl[b-1].append((c,a-1))

a,u,q=1,[0]*n,[]
u[0]=1
for c,v in gl[0]:heappush(q,(c,v))

for x in list(map(int,input().split())):
    l=[]
    while q and q[0][0]<=x:
        _,v=heappop(q)
        if u[v]:continue
        u[v]=1
        a+=1
        for d,t in gl[v]:l.append((d,t))
    print(a)
    for d,t in l:heappush(q,(d,t))