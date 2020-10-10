def warshall_floyd(d,n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d


def main():
    n,m,r = map(int, input().split())
    rl = list(map(int, input().split()))
    rl = [r-1 for r in rl]
    INF = 10**18
    d = [ [INF]*n for _ in range(n) ]
    for _ in range(m):
        a,b,c = map(int, input().split())
        a-=1
        b-=1
        d[a][b] = c
        d[b][a] = c

    d = warshall_floyd(d,n)
    g = [ [INF]*r for _ in range(r) ]
    for i in range(r):
        for j in range(r):
            g[i][j] = d[rl[i]][rl[j]]
            g[j][i] = d[rl[j]][rl[i]]


    ans = INF
    for start in range(r):
        dp = [ [INF]*r for _ in range(2**r)]
        dp[1<<start][start] = 0
        for i in range(2**r):
            for j in range(r):
                for k in range(r):
                    if i&(1<<k) == 0:
                        dp[i|(1<<k)][k] = min(dp[i|(1<<k)][k], dp[i][j]+g[j][k])
        ans = min(ans, min(dp[2**r-1]))
    print(ans)


if __name__ == "__main__":
    main()