from collections import deque
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


h,w =map(int, input().split())
al = [list(input()) for _ in range(h)]
alp_d = {chr(ord('a') + i): [] for i in range(26)}

g = [ [] for _ in range(h*w+26)]
s = -1
goal = -1

# for hi in range(h):
#     row = list(input())
#     al.append(row)
#     for wi in range(w):
#         v = row[wi]
#         if v == 'S':
#             s = hi*w+wi
#         elif v == 'G':
#             goal = hi*w+wi
#         elif v == '#' or v == '.':
#             pass
#         else:
#             super_v = ord(v)-ord('a') + h*w
#             g[super_v].append()

for hi in range(h):
    for wi in range(w):
        curr = al[hi][wi]
        if curr == '#': continue

        u = hi*w+wi
        if curr == 'S':
            s = hi*w+wi
        elif curr == 'G':
            goal = hi*w+wi
        elif curr != '.':
            super_v = ord(curr)-ord('a') + h*w
            g[super_v].append((u,0))
            g[u].append((super_v,1))

        if hi+1 < h and al[hi+1][wi] != '#':
            v = (hi+1)*w+wi
            g[u].append((v,1))
            g[v].append((u,1))
        if wi+1 < w and al[hi][wi+1] != '#':
            v = hi*w+wi+1
            g[u].append((v,1))
            g[v].append((u,1))


# for i in range(26):
#     super_v = h*w+i
#     for av in alp_d[chr(ord('a') + i)]:
#         g[av].append((super_v,1))
#         g[super_v].append((av,0))


ansd = dijkstra(s, h*w+26, g)
ans = ansd[goal]
if ans == INF: ans=-1
print(ans)