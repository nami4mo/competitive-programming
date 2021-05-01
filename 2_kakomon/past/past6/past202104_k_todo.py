R=100
dp=[-10**9]*R
dp[0]=0
for _ in range(int(input())):
    p,u=map(int, input().split())
    ndp=dp[:]
    for i in range(R):
        r=(i+p)%R
        c=((i+p)//R)*20
        ndp[r]=max(ndp[r],dp[i]+u-p+c)
    dp=ndp[:]
print(max(dp))