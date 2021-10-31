def warshall_floyd(d,n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

INF=10**18
n,m=map(int, input().split())
d=[[INF]*n for _ in range(n)]
for _ in range(m):
    a,b,c=map(int, input().split())
    a-=1
    b-=1
    d[a][b]=c

ans=0
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j],d[i][k] + d[k][j])
            # print(i,j)
            # print(d[i][j])
            if d[i][j]<INF and i!=j:ans+=d[i][j]
print(ans)