import heapq
def dijkstra(s, n, g, d): # s: start, n: |V|, g; glaph 
    INF = 10**20
    # d = [INF] * n
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


def main():
    n,m,s = map(int, input().split())
    if s > 2500: s = 2500
    # g = [ [] for _ in range(n*2500+1)]
    g = {}
    dist = {}
    for i in range(n):
        for j in range(2501):
            g[(i,j)] = []
            dist[(i,j)] = 10**20

    for _ in range(m):
        u,v,a,b =map(int, input().split())
        u-=1
        v-=1
        for j in range(2501):
            if j-a >= 0:
                g[(u,j)].append( ((v,j-a), b) )
                g[(v,j)].append( ((u,j-a), b) )

    for i in range(n):
        c,d = map(int, input().split())
        for j in range(2500):
            if j+c <= 2500:
                g[(i,j)].append( ((i,j+c), d) )

    ans = dijkstra((0,s), len(g), g, dist)
    # print(ans)
    for i in range(1,n):
        mv = 10**20
        for j in range(2501):
            mv = min(mv, ans[(i,j)])
        print(mv)



if __name__ == "__main__":
    main()