def warshall_floyd(d,n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

h, w = map(int, input().split())
c = [ list(map(int, input().split())) for _ in range(10) ]

num_cnt = [0]*10
for _ in range(h):
    al = list(map(int, input().split()))
    for a in al:
        if a >= 0: num_cnt[a] += 1

warshall_floyd(c,10)

ans = 0
for num, cnt in enumerate(num_cnt):
    ans += c[num][1] * cnt

print(ans)