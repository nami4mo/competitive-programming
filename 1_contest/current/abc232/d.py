

def main():
    h, w = map(int, input().split())
    cl = []
    for _ in range(h):
        cl.append(list(input()))

    from collections import deque
    q = deque()
    d = [[-1]*w for _ in range(h)]
    d[0][0] = 0
    q.append((0, 0))
    while q:
        y, x = q.popleft()
        for dy, dx in [(1, 0), (0, 1)]:
            yy = dy+y
            xx = dx+x
            if yy >= h or xx >= w:
                continue
            if d[yy][xx] != -1:
                continue
            if cl[yy][xx] == '#':
                continue
            d[yy][xx] = d[y][x]+1
            q.append((yy, xx))
    ans = 0
    for row in d:
        ans = max(ans, max(row))
    print(ans+1)
    # print(d)


if __name__ == "__main__":
    main()
