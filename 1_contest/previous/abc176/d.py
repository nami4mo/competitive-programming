from collections import deque
def bfs(sl, visited, sy, sx, gy, gx, h, w):
    q = deque([[sy,sx]])
    visited[sy][sx] = 0
    qn = deque([[sy,sx]])

    while q:
        # print('---q')
        while q:
            y, x = q.popleft()
            qn.append([y,x])
            if [y, x] == [gy, gx]:
                return visited[gy][gx]
            for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
                ny, nx = y+j, x+k
                if ny >= h or nx >= w or ny < 0 or nx < 0:
                    continue
                if sl[ny][nx] == '.' and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x]
                    q.append([ny,nx])
                    qn.append([ny,nx])
        #     print(q)
        #     print(qn)
        #     print()
            
        # print('---------qn')
        next_qnl = []
        while qn:
            y, x = qn.popleft()
            # q.append([y,x])
            for j in range(-2,3):
                for k in range(-2,3):
                    ny, nx = y+j, x+k
                    if ny >= h or nx >= w or ny < 0 or nx < 0: continue
                    if sl[ny][nx] == '.' and visited[ny][nx] == -1:
                        visited[ny][nx] = visited[y][x] + 1
                        # qn.append([ny,nx])
                        q.append([ny,nx])
            # print(q)
            # print(qn)
            # print()

    return -1


h, w = map(int, input().split()) 
ch,cw = map(int, input().split())
dh,dw = map(int, input().split())
sl = [list(input()) for _ in range(h)]
visited = [ [-1]*w for i in range(h)]
ans = bfs(sl,visited,ch-1,cw-1,dh-1,dw-1,h,w)
print(ans)