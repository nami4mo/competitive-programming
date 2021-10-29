import heapq
INF = 10**18

def dijkstra(s, n, g, not_u=-1, not_v=-1): # s: start, n: |V|, g; glaph (to,cost)
    d = [INF] * n
    #-- record the prev vertex of each one for restoring the route --
    prev_vl = [-1]*n 
    d[s] = 0
    que = [] # (a,b): a... shortest dist, b... v
    heapq.heappush(que, (0, s))

    while que:
        dist, v = heapq.heappop(que)
        if d[v] < dist: continue # if v has been already used -> continue
        for next_v, cost in g[v]:
            if v==not_u and next_v==not_v:continue
            if d[next_v] > d[v] + cost:
                d[next_v] = d[v] + cost
                prev_vl[next_v] = v
                heapq.heappush(que, (d[next_v], next_v))

    if not_u!=-1:
        return d, []

    ## resotre the route
    goal = n-1 # set goal here (do you need loop?)
    route = [goal]
    curr_v = goal
    while True:
        prev_v = prev_vl[curr_v]
        if prev_v == -1: break
        route.append(prev_v)
        curr_v = prev_v
    route = route[::-1]
    return d, route
    return d


n,m=map(int, input().split())
gl=[[] for _ in range(n)]
st2e=[[-1]*n for _ in range(n) ]
for i in range(m):
    s,t=map(int, input().split())
    s-=1
    t-=1
    gl[s].append((t,1))
    st2e[s][t]=i

dist,route=dijkstra(0,n,gl)
ans=dist[n-1]
if ans>=INF:ans=-1
ansl=[ans]*m
for i in range(len(route)-1):
    u=route[i]
    v=route[i+1]
    ei=st2e[u][v]
    dist,_=dijkstra(0,n,gl,u,v)
    ans=dist[n-1]
    if ans>=INF:ans=-1
    ansl[ei]=ans
for v in ansl:
    print(v)