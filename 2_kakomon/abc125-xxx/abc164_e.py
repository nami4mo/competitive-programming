import heapq
def dijkstra(s, n, g, d): # s: start, n: |V|, g; glaph 
    INF = 10**18
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
    g = {}
    dist = {}
    for i in range(n):
        for j in range(2501):
            g[(i,j)] = []
            dist[(i,j)] = 10**18
    for _ in range(m):
        u,v,a,b = map(int, input().split())
        u-=1
        v-=1
        for j in range(2501):
            if j < a: continue
            g[(u,j)].append(((v,j-a),b))
            g[(v,j)].append(((u,j-a),b))

    for i in range(n):
        c,d = map(int, input().split())
        for j in range(2501):
            maxc = min(2500,j+c)
            g[(i,j)].append(((i,maxc), d))

    sc = min(2500,s)
    s = (0,sc)
    dist = dijkstra(s, n*2501+1, g, dist)
    for i in range(1,n):
        ans = 10**18
        for j in range(2501):
            ans = min(ans, dist[(i,j)])
        print(ans)

if __name__ == "__main__":
    main()