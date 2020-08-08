INF = 10**12

def warshall_floyd(d,n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d


def main():

    n,m,l = map(int, input().split())
    d = [ [INF]*(n) for _ in range(n) ]
    for _ in range(m):
        a,b,c = map(int, input().split())
        d[a-1][b-1] = c
        d[b-1][a-1] = c

    warshall_floyd(d, n)

    d2 = [ [INF]*(n) for _ in range(n) ]
    for i in range(n):
        for j in range(n):
            if d[i][j] <= l:
                d2[i][j] = 1

    warshall_floyd(d2,n)
    ans = []
    q = int(input())
    for _ in range(q):
        s,t = map(int, input().split())
        dist = d2[s-1][t-1]
        if dist == INF: dist = 0
        # ans.append(dist-1)
        print(dist-1)

    # for a in ans:
    #     print(a)

if __name__ == "__main__":
    main()