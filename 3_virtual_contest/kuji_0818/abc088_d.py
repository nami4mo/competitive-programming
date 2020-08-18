from collections import deque
def bfs(sl, visited, sy, sx, gy, gx, h, w):
    q = deque([[sy,sx]])
    visited[sy][sx] = 0
    while q:
        y, x = q.popleft()
        if [y, x] == [gy, gx]:
            return visited[gy][gx]
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            ny, nx = y+j, x+k
            if ny >= h or nx >= w or ny < 0 or nx < 0:
                continue
            if sl[ny][nx] == '.' and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append([ny,nx])
    return -1


def main():
    h,w = map(int, input().split())
    sl = []
    white = 0
    for _ in range(h):
        row = list(input())
        white += row.count('.')
        sl.append(row)

    visited = [ [-1]*w for i in range(h)]
    bfs(sl, visited, 0, 0, h-1, w-1, h, w)
    dist = visited[h-1][w-1]
    if dist == -1:
        print(-1)
    else:
        ans = white - dist - 1
        print(ans)





if __name__ == "__main__":
    main()