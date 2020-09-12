def warshall_floyd(d,n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d


def main():
    INF = 10**18
    n,m,l = map(int, input().split())
    d = [ [INF]*(n+1) for _ in range(n+1) ]
    for _ in range(m):
        a,b,c = map(int, input().split())
        d[a][b] = c
        d[b][a] = c

    d = warshall_floyd(d,n+1)
    new_d = [ [INF]*(n+1) for _ in range(n+1) ]
    for a in range(n+1):
        for b in range(n+1):
            if d[a][b] <= l:
                new_d[a][b] = 1
                new_d[b][a] = 1


    new_d = warshall_floyd(new_d,n+1)
    ansl = []
    q = int(input())
    for _ in range(q):
        s,t = map(int, input().split())
        ans = new_d[s][t]
        if ans >= INF: ans = 0
        ansl.append(ans-1)

    for a in ansl: print(a)



if __name__ == "__main__":
    main()