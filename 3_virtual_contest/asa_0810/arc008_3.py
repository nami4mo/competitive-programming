import math
import heapq

def dijkstra(s, n, g):
    INF = 10**10
    d = [INF] * n
    d[s] = 0
    que = [] # (a,b): a... shortest dist, b... v
    heapq.heapify(que)
    heapq.heappush(que, (0, s))

    while que:
        dist, v = heapq.heappop(que)
        if d[v] < dist: continue # if v has been already used -> continue
        for edge in g[v]:
            to, cost = edge
            if d[to] > d[v] + cost:
                d[to] = d[v] + cost
                heapq.heappush(que, (d[to], to))
    return d


def main():
    n = int(input())
    if n == 1:
        print(0)
        exit()

    xytrl = []
    for _ in range(n):
        x,y,t,r = map(int, input().split())
        xytrl.append((x,y,t,r))

    gl = [ [] for _ in range(n) ]
    for i in range(n):
        for j in range(n):
            if i == j : continue
            xi,yi,ti,ri = xytrl[i]
            xj,yj,tj,rj = xytrl[j]
            dist = math.sqrt((xi-xj)**2+(yi-yj)**2)
            speed = min(ti,rj)
            t = dist/speed
            gl[i].append((j,t))



    d = dijkstra(0, n, gl)
    ansl = d[1:]
    ansl.sort(reverse=True)
    for i in range(n-1):
        ansl[i] += (i)

    print(max(ansl))


if __name__ == "__main__":
    main()