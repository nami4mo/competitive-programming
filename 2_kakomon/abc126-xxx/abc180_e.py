n=int(input())
xyzl=[]
for _ in range(n):
    x,y,z=map(int, input().split())
    xyzl.append((x,y,z))

INF=10**18
gl = [ [INF]*(n) for _ in range(n)]
for i in range(n):
    for j in range(n):
        x,y,z=xyzl[i]
        xx,yy,zz=xyzl[j]
        d=abs(x-xx)+abs(y-yy)+max(0,zz-z)
        gl[i][j]=d


dp = [ [INF]*(n) for _ in range(2**n) ]
dp[1][0] = 0
for i in range(2**n):
    for j in range(n):
        if dp[i][j] == INF: continue
        for k in range(n):
            if (i>>k)%2 == 1: continue
            dp[i|(1<<k)][k] = min(dp[i][j]+gl[j][k], dp[i|(1<<k)][k])

ans = INF
for i in range(1,n): 
    if gl[i][0] != INF:
        ans = min(ans, dp[2**n-1][i] + gl[i][0])

if ans == INF: ans = -1
print(ans)