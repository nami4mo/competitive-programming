import heapq
INF = 10**18
def dijkstra(s, n, g): # s: start, n: |V|, g; glaph 
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
gl=[ [] for _ in range(n*3) ]

for _ in range(m):
    u,v=map(int, input().split())
    u-=1
    v-=1
    gl[3*u+0].append((3*v+1,1))
    gl[3*u+1].append((3*v+2,1))
    gl[3*u+2].append((3*v+0,1))

s,t=map(int, input().split())
s-=1
t-=1
d=dijkstra(s*3,n*3,gl)
ans=d[t*3]
if ans==INF: ans=-3
print(ans//3)