def warshall_floyd(d,n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

INF = 10**9
n,m = map(int, input().split())
d = [ [INF]*n for _ in range(n) ]
dorig = [ [INF]*n for _ in range(n) ]

for i in range(n):
    d[i][i] = 0
    dorig[i][i] = 0
for _ in range(m):
    a,b,c = map(int, input().split())
    d[a-1][b-1] = min(d[a-1][b-1], c)
    d[b-1][a-1] = min(d[b-1][a-1], c)
    dorig[a-1][b-1] = min(dorig[a-1][b-1], c)
    dorig[b-1][a-1] = min(dorig[b-1][a-1], c)

# print(d)
d = warshall_floyd(d,n)
# print(d)

ans = 0
for i in range(n):
    for j in range(i+1,n):
        ans += d[i][j]

k=int(input())
ansl = []
for _ in range(k):
    a,b,c = map(int, input().split())
    if dorig[a-1][b-1] <= c:
        # print(ans)
        ansl.append(ans)
    else:
        dorig[a-1][b-1] = c
        dorig[b-1][a-1] = c
        curr_ans = 0
        for i in range(n):
            for j in range(i+1,n):
                v1 = d[i][j]
                v2 = d[i][a-1] + dorig[a-1][b-1] + d[b-1][j]
                v3 = d[i][b-1] + dorig[b-1][a-1] + d[a-1][j]
                v4 = min(v2,v3)
                if v1 < v4:
                    curr_ans += v1
                else:
                    curr_ans += v4
                    d[i][j] = v4
                    d[j][i] = v4
        # print(curr_ans)
        ansl.append(curr_ans)
        ans = curr_ans

for a in ansl: print(a)