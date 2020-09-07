for _ in range(int(input())):
    n,m = map(int, input().split())
    al = [list(input()) for _ in range(n)]
    ans = 0
    for ni in range(n):
        if al[ni][-1] == 'R': ans += 1
    for mi in range(m):
        if al[-1][mi] == 'D': ans += 1

    print(ans)