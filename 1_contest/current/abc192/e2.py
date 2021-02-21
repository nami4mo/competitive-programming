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
        for next_v, cost, k in g[v]:
            start_d=dist
            rem=start_d%k
            if rem!=0:start_d+=(k-rem)
            next_d=start_d+cost
            if d[next_v] > next_d:
                d[next_v] = next_d
                heapq.heappush(que, (d[next_v], next_v))
    return d


n,m,x,y=map(int, input().split())
x-=1
y-=1
gl=[[] for _ in range(n)]
for i in range(m):
    a,b,t,k=map(int, input().split())
    a-=1
    b-=1
    gl[a].append((b,t,k))
    gl[b].append((a,t,k))

dl=dijkstra(x,n,gl)
ans=dl[y]
if ans>=10**18:ans=-1
print(ans)