from collections import deque
from bisect import bisect_left

n = int(input())
al = list(map(int, input().split()))
g = [ [] for _ in range(n)]
for _ in range(n-1):
    u,v = map(int, input().split())
    u-=1
    v-=1
    g[u].append(v)
    g[v].append(u)

INF = 10**10
dp = [INF]*(n+1)
dp[0] = -INF

hist = [(-1,-1)]*n
visited = [False]*n
q = deque([(0,-1,-1)])
ansl = [-1]*n
while q:
    curr_node, prev_ind, prev_v = q.popleft()
    if visited[curr_node]:
        dp[prev_ind] = prev_v
        # print('--skip===')
        # print(curr_node+1)
        # print(prev_ind,prev_v)
        # print(dp)
        continue 
    ind = bisect_left(dp, al[curr_node])
    orig = dp[ind]
    dp[ind] = al[curr_node]
    ans = bisect_left(dp, INF) - 1
    ansl[curr_node] = ans
    # print('-----')
    # print(curr_node+1)
    # print(dp)
    hist[curr_node] = (ind,al[curr_node])
    visited[curr_node] = True
    novis = []
    for next_node in g[curr_node]:
        if not visited[next_node]: novis.append(next_node)
        else:q.appendleft((next_node,ind,orig))
    for v in novis: q.appendleft((v,ind,orig))


for a in ansl: print(a)