# 謎に無駄なことをしてしまったけど、記念として残す

from collections import deque
def bfs(start, g, visited):
    q = deque([])
    k_neibs = g[start]
    visited[start] = (0,start)
    for neib, dist in k_neibs:
        q.append((neib, neib)) # node, root parent (k neib)
        visited[neib] = (dist, neib) # dist, root parent (k neib)

    while q:
        curr_node, root_pare = q.popleft()
        for next_node, dist in g[curr_node]:
            if visited[next_node] != (-1,-1): continue
            curr_dist = visited[curr_node][0]
            visited[next_node] = (curr_dist+dist, root_pare)
            q.append((next_node, root_pare))


def main():
    n = int(input())
    g = [ [] for _ in range(n+1)]
    for _ in range(n-1):
        a, b, c = map(int, input().split()) 
        g[a].append((b,c))
        g[b].append((a,c))

    q,k = map(int, input().split())
    visited = [(-1,-1)] * (n+1) # dist, root parent (k neib)
    bfs(k, g, visited)

    ansl = []
    for _ in range(q):
        x,y = map(int, input().split())
        xd, xp = visited[x]
        yd, yp = visited[y]
        # めっちゃ無駄なことしてたーーーーーーーー！
        if xp == yp:
            ans = xd+yd
            ansl.append(ans)
        else:
            ans = xd+yd
            ansl.append(ans)

    for a in ansl: print(a)

if __name__ == "__main__":
    main()