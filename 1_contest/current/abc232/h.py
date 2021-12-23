import heapq


def dijkstra(s, n, g):  # s: start, n: |V|, g; glaph (to,cost)
    INF = 10**18
    d = [INF] * n
    # -- record the prev vertex of each one for restoring the route --
    prev_vl = [-1]*n
    d[s] = 0
    que = []  # (a,b): (a: shortest dist, b: node)
    heapq.heappush(que, (0, s))

    while que:
        dist, v = heapq.heappop(que)
        if d[v] < dist:
            continue  # if v has been already used -> continue
        for next_v, cost in g[v]:
            if d[next_v] > d[v] + cost:
                d[next_v] = d[v] + cost
                prev_vl[next_v] = v
                heapq.heappush(que, (d[next_v], next_v))
    # resotre the route
    goal = n-1  # set goal here (do you need loop?)
    route = [goal]
    curr_v = goal
    while True:
        prev_v = prev_vl[curr_v]
        if prev_v == -1:
            break
        route.append(prev_v)
        curr_v = prev_v
    route = route[::-1]
    return d, route
    # return d


def main():
    n, m = map(int, input().split())
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))
    gl = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            d = (al[i]+bl[j]) % m
            gl[i].append((j, d))
    d, r = dijkstra(0, n, gl)
    print(d)
    print(r)


if __name__ == "__main__":
    main()
