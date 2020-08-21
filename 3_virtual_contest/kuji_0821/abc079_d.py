def warshall_floyd(d,n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d


h,w = map(int, input().split())
cl = [list(map(int, input().split())) for _ in range(10)]
cl = warshall_floyd(cl,10)

al = [list(map(int, input().split())) for _ in range(h)]
ans = 0
for row in al:
    for a in row:
        if a == -1:continue
        ans += cl[a][1]
print(ans)