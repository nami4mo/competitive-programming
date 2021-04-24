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

n,m=map(int, input().split())
gl=[[] for _ in range(n)]
for _ in range(m):
    a,b,c=map(int, input().split())
    a-=1
    b-=1
    gl[a].append((b,c))
    gl[b].append((a,c))

d1=dijkstra(0,n,gl)
d2=dijkstra(n-1,n,gl)
for i in range(n):
    ans=d1[i]+d2[i]
    print(ans)