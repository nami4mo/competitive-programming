from collections import deque
def bfs(sl, visited, sy, sx, gy, gx, h, w):
    q = deque([[sy,sx]])
    q_warp = deque([])
    visited[sy][sx] = 0

    while q:
        while q:
            y, x = q.popleft()
            q_warp.append([y,x])
            if [y, x] == [gy, gx]:
                return visited[gy][gx]
            for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
                ny, nx = y+j, x+k
                if ny >= h or nx >= w or ny < 0 or nx < 0:
                    continue
                if sl[ny][nx] == '.' and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x]
                    q.append([ny,nx])

        while q_warp:
            y, x = q_warp.popleft()
            for j in range(-2,3):
                for k in range(-2,3):
                    ny, nx = y+j, x+k
                    if ny >= h or nx >= w or ny < 0 or nx < 0: continue
                    if sl[ny][nx] == '.' and visited[ny][nx] == -1:
                        visited[ny][nx] = visited[y][x] + 1
                        q.append([ny,nx])

    return -1


h, w = map(int, input().split()) 
ch,cw = map(int, input().split())
dh,dw = map(int, input().split())
sl = [list(input()) for _ in range(h)]
visited = [ [-1]*w for i in range(h)]
ans = bfs(sl,visited,ch-1,cw-1,dh-1,dw-1,h,w)
print(ans)