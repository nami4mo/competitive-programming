n,m=map(int, input().split())
al=list(map(int, input().split()))
gl=[[] for _ in range(n)]
for _ in range(m):
    x,y=map(int, input().split())
    x-=1
    y-=1
    gl[x].append(y)

dp=[10**18]*n
dp[0]=al[0]
ans=-10**18
for i in range(n):
    dp[i]=min(dp[i],al[i])
    for to in gl[i]:
        gain=al[to]-dp[i]
        dp[to]=min(dp[to], dp[i], al[to])
        ans=max(gain,ans)
print(ans)