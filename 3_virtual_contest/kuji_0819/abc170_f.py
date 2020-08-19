import sys
from collections import deque
input = sys.stdin.readline

def bfs(sl, visited, sy, sx, gy, gx, h, w, k):
    q = deque([ (sy,sx) ])
    visited[sy][sx] = 0
    while q:
        # print(q)
        y, x = q.popleft()
        if [y, x] == [gy, gx]:
            return visited[gy][gx]
        for i in range(1,k+1):
            ny = y+i
            if ny >= h:
                break
            if sl[ny][x] == '@':
                break
            if 0 <= visited[ny][x] <= visited[y][x]:
                break
            if visited[ny][x] != visited[y][x]+1: 
                visited[ny][x] = visited[y][x]+1
                q.append((ny,x))

        for i in range(1,k+1):
            ny = y-i
            if ny < 0:
                break
            if sl[ny][x] == '@':
                break
            if 0 <= visited[ny][x] <= visited[y][x]:
                break
            if visited[ny][x] != visited[y][x]+1: 
                visited[ny][x] = visited[y][x]+1
                q.append((ny,x))

        for i in range(1,k+1):
            nx = x+i
            if nx >= w:
                break
            if sl[y][nx] == '@':
                break
            if 0 <= visited[y][nx] <= visited[y][x]:
                break
            if visited[y][nx] != visited[y][x]+1: 
                visited[y][nx] = visited[y][x]+1
                q.append((y,nx))

        for i in range(1,k+1):
            nx = x-i
            if nx < 0:
                break
            if sl[y][nx] == '@':
                break
            if 0 <= visited[y][nx] <= visited[y][x]:
                break
            if visited[y][nx] != visited[y][x]+1: 
                visited[y][nx] = visited[y][x]+1
                q.append((y,nx))

    return -1

def main():
    h,w,k = map(int, input().split())
    x1,y1,x2,y2 = map(int, input().split())
    cl = []
    for i in range(h):
        row = list(input())
        cl.append(row)

    visited = [ [-1]*w for i in range(h)]
    ans = bfs(cl, visited, x1-1,y1-1,x2-1,y2-1,h,w,k)
    print(ans)

if __name__ == "__main__":
    main()