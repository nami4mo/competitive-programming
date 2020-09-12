import heapq
def dijkstra(s, n, g): # s: start, n: |V|, g; glaph 
    INF = 10**18
    d = [INF] * n
    d[s] = 0
    que = [] # (a,b): a... shortest dist, b... v
    heapq.heappush(que, (0, s))

    while que:
        dist, v = heapq.heappop(que)
        if d[v] < dist: continue # if v has been already used -> continue
        for next_v, cost in g[v]:
            if d[next_v] > d[v] + cost:
                d[next_v] = d[v] + cost
                heapq.heappush(que, (d[next_v], next_v))
    return d


def main():
    n,m,s = map(int, input().split())
    g = [ [] for _ in range(n*2501+1)]
    for _ in range(m):
        u,v,a,b = map(int, input().split())
        u-=1
        v-=1
        for j in range(2501):
            if j < a: continue
            g[u*2501+j].append((v*2501+j-a,b))
            g[v*2501+j].append((u*2501+j-a,b))


    cdl = [(-1,-1)]
    for i in range(n):
        c,d = map(int, input().split())
        for j in range(2501):
            maxc = min(2500,j+c)
            g[i*2501+j].append((i*2501+maxc,d))

    s = min(2500,s)
    dist = dijkstra(s, n*2501+1, g)
    # print(dist)
    for i in range(1,n):
        ans = min(dist[i*2501:i*2501+2500])
        print(ans)


if __name__ == "__main__":
    main()