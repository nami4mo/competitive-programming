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

n,m,l=map(int, input().split())
MAX=1001
gl=[[] for _ in range(n*MAX)]
for _ in range(m):
    a,b,c=map(int, input().split())
    a-=1
    b-=1
    for j in range(MAX-1):
        gl[a*MAX+j].append((b*MAX+j,c))
        gl[b*MAX+j].append((a*MAX+j+1,c))

d=dijkstra(0,n*MAX,gl)
# print(d)

for i in range(MAX):
    if d[(n-1)*MAX+i]<=l:
        print(i)
        break
else:
    print(-1)