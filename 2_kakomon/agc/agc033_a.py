from collections import deque
def bfs(al, h, w):
    q = deque([])
    visited = [ [-1]*w for _ in range(h) ]
    for i in range(h):
        for j in range(w):
            if al[i][j] == '#': 
                q.append((i,j))
                visited[i][j] = 0

    while q:
        i, j = q.popleft()
        for ver, hor in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            ni, nj = i+ver, j+hor
            if ni >= h or nj >= w or ni < 0 or nj < 0:
                continue
            if al[ni][nj] == '.' and visited[ni][nj] == -1:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni,nj))
    return visited


def main():
    h,w = map(int, input().split())
    al = []
    for _ in range(h):
        row = list(input())
        al.append(row)

    visited = bfs(al,h,w)
    ans = 0
    for v in visited:
        ans = max(max(v),ans)

    print(ans)

if __name__ == "__main__":
    main()