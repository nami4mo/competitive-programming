import heapq
def dijkstra(s, n, g): # s: start, n: |V|, g; glaph (to,cost)
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


k=int(input())
gl=[[] for _ in range(k)]
for i in range(1,k):
    for j in range(10):
        to=(i*10+j)%k
        gl[i].append((to,j))
d=dijkstra(1,k,gl)
print(d[0]+1)