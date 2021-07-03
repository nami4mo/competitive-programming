import heapq
INF = 10**18
def dijkstra(s, n, g): # s: start, n: |V|, g; glaph (to,cost)
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

n,m=map(int, input().split())
gl=[[] for _ in range(n+m)]

for i in range(m):
    k=int(input())
    rl=list(map(int, input().split()))
    for r in rl:
        gl[r-1].append((n+i,0))
        gl[n+i].append((r-1,1))

d=dijkstra(0,n+m,gl)
for i in range(n):
    ans=d[i]
    if ans>=INF:ans=-1
    print(ans)