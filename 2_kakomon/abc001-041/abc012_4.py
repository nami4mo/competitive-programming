
def warshall_floyd(d,n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

n,m=map(int, input().split())
INF=10**10
d=[[INF]*n for _ in range(n)]
for i in range(n): d[i][i]=0
for _ in range(m):
    a,b,t=map(int, input().split())
    a-=1
    b-=1
    d[a][b]=t
    d[b][a]=t

d=warshall_floyd(d,n)
ans_i=-1
ans_v=INF
for i in range(n):
    v=0
    for j in range(n):
        v=max(v,d[i][j])
    if v<=ans_v:
        ans_i=i
        ans_v=v

print(ans_v)