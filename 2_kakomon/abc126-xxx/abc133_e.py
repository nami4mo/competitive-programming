from collections import deque
MOD = 10**9+7

def bfs(start, g, visited, k):
    q = deque([start])
    visited[start] = 0
    ans = k
    first_flag = True
    while q:
        curr_node = q.popleft()
        i = 0
        for next_node in g[curr_node]:
            if visited[next_node] >= 0: continue
            if first_flag: 
                ans *= (k-(i+1))
            else:
                ans *= (k-(i+2))
            ans%=MOD
            visited[next_node] = visited[curr_node] + 1
            q.append(next_node)
            i+=1
        first_flag = False
    return ans


n, k = map(int, input().split()) 
g = [ [] for _ in range(n+1)]
visited = [-1] * (n+1)
for i in range(n-1):
    a, b = map(int, input().split()) 
    g[a].append(b)
    g[b].append(a)

ans = bfs(1, g, visited, k)
print(ans)