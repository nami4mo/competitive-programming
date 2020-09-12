from collections import deque
def bfs(start, g, visited, goal):
    q = deque([start])
    visited[start] = 0
    while q:
        curr_node = q.popleft()
        for next_node in g[curr_node]:
            if visited[next_node] >= 0: continue
            visited[next_node] = visited[curr_node] + 1
            if next_node == goal: return
            q.append(next_node)


n,m = map(int, input().split())
g = [ [] for _ in range(3*n)]

for _ in range(m):
    u,v = map(int, input().split())
    g[u*3-3].append(v*3-2)
    g[u*3-2].append(v*3-1)
    g[u*3-1].append(v*3-3)

s,t = map(int, input().split())
visited = [-3]*(3*n)
bfs(s*3-3, g, visited, t*3-3)
print(visited[t*3-3]//3)