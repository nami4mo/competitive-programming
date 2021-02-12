from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def bfs(n, k, s, goals, g):
    visited = [-1 for _ in range(n+1)]
    q = deque([s])
    visited[s] = 0
    res = [-1 for _ in range(k)]
    goal_cnt = 0
    while q:
        curr = q.popleft()
        if curr in goals:
            goal_cnt += 1
            goad_i = goals.index(curr)
            res[goad_i] = visited[curr]
            if goal_cnt == k:
                return res
        for neib in g[curr]:
            if visited[neib] == -1:
                visited[neib] = visited[curr] + 1
                q.append(neib)      



#訪れた集合がs、今いる点がvの時０に戻る最短経路
def rec(s,v,dp,   k,d):
    if dp[s][v] >= 0:
        return dp[s][v]
        
    if s == (1<<k)-1:
        #全ての頂点を訪れた(s = 11...11 and v = 0)
        for aaa in dp[s]:
            aaa = 0
        # dp[s][] = 0
        return 0
    
    res = float("inf")
    for u in range(k):
        if (s>>u&1) == 0:
            #uに訪れていない時(uの箇所が0の時),次はuとすると
            res = min(res,rec(s|(1<<u),u,dp, k,d )+d[v][u])
            
    dp[s][v] = res
    return res


def main():
    n, m = map(int, input().split()) 
    g = [ [] for _ in range(n+1)]

    for _ in range(m):
        u, v = map(int, input().split()) 
        g[u].append(v)
        g[v].append(u)

    s = int(input())
    k = int(input())
    tl = list(map(int, input().split())) 
    s_tl = [s]
    s_tl.extend(tl)

    # s_to_tl = bfs(n,k,s, tl, g)
    t_to_tls = []
    for t in s_tl:
        t_to_tls.append( bfs(n,k+1,t,s_tl,g) )
    # print(t_to_tls)

    dp = [[-1] * (k+1) for i in range(1<<(k+1))]
    
    ans = rec(0,0,dp, k+1,t_to_tls)
    print(ans)


if __name__ == "__main__":
    main()
