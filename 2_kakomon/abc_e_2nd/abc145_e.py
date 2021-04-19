n,t=map(int, input().split())
abl=[]
for _ in range(n):
    a,b=map(int, input().split())
    abl.append((a,b))
abl.sort()
dp=[[0]*(t) for _ in range(n+1)]

ans=0
for i in range(n):
    cost,val=abl[i]
    for j in range(t):
        dp[i+1][j]=max(dp[i+1][j],dp[i][j])
        ans=max(dp[i+1][j], ans)
        if j+cost>=t: ans=max(ans, dp[i][j]+val)
        else:
            dp[i+1][j+cost]=max(dp[i+1][j+cost], dp[i][j]+val)
            ans=max(dp[i+1][j+cost], ans)
print(ans)