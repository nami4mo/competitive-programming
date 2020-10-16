from heapq import heapify, heappop, heappush

n = int(input())
hq = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(i+1,n):
        heappush(hq,(row[j],i,j))

INF = 10**18
d = [[INF]*n for _ in range(n)]

ans = 0
while hq:
    dist, u, v = heappop(hq)
    # print(dist,u,v)
    # print(d[u][v])
    # print()
    if d[u][v] > dist:
        ans += dist
        d[u][v] = dist
        d[v][u] = dist
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][u]+d[u][j], d[i][v]+d[v][j], d[i][u]+dist+d[v][j], d[i][v]+dist+d[u][j])
    elif d[u][v] == dist:
        pass
    else:
        print(-1)
        exit()

print(ans)