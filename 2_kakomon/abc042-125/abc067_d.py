from collections import deque
def bfs(G, n,visited):
    q = deque([(1,'fe'),(n,'su')])
    visited[1] = 'fe'
    visited[n] = 'su'
    while q:
        curr_node = q.popleft()
        for next_node in G[curr_node[0]]:
            if visited[next_node] != 'yet': continue
            visited[next_node] = curr_node[1]
            q.append((next_node,curr_node[1]))


n = int(input())
G = [ [] for _ in range(n+1)]
visited = ['yet'] * (n+1)
for i in range(n-1):
    a, b = map(int, input().split()) 
    G[a].append(b)
    G[b].append(a)
bfs(G, n, visited)

if visited.count('fe') > visited.count('su'):
    print('Fennec')
else:
    print('Snuke')