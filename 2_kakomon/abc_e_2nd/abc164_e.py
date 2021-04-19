import heapq
def dijkstra(s, n, g): # s: start, n: |V|, g; glaph 
    INF = 10**18
    d = [INF] * n
    #-- record the prev vertex of each one for restoring the route --
    # prev_vl = [-1]*n 
    d[s] = 0
    que = [] # (a,b): a... shortest dist, b... v
    heapq.heappush(que, (0, s))

    while que:
        dist, v = heapq.heappop(que)
        if d[v] < dist: continue # if v has been already used -> continue
        for next_v, cost in g[v]:
            if d[next_v] > d[v] + cost:
                d[next_v] = d[v] + cost
                # prev_vl[next_v] = v
                heapq.heappush(que, (d[next_v], next_v))
    return d

n,m,s=map(int, input().split())
gl=[ [] for _ in range(n*2501)]
for _ in range(m):
    u,v,a,b=map(int, input().split())
    u-=1
    v-=1
    for i in range(a,2501):
        uu=u*2501+i
        vv=v*2501+i-a
        gl[uu].append((vv,b))
        uu=u*2501+i-a
        vv=v*2501+i
        gl[vv].append((uu,b))

for i in range(n):
    c,d=map(int, input().split())
    for j in range(2501):
        cnt=min(2500,j+c)
        u=i*2501+j
        v=i*2501+cnt
        gl[u].append((v,d))
        gl[u].append((i*2501,0))

s=min(s,2500)
d=dijkstra(s,n*2501,gl)
for i in range(1,n):
    ans=d[i*2501]
    print(ans)