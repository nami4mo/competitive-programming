ansl=[]
for _ in range(int(input())):
    n=int(input())
    al=list(map(int, input().split()))
    al.sort()
    MAX_T=400
    dp=[[10**10]*(n+1) for _ in range(MAX_T)]
    dp[0][0]=0
    for t in range(MAX_T-1):
        for j in range(n+1):
            dp[t+1][j]=min(dp[t+1][j],dp[t][j])
            if j!=n:
                dp[t+1][j+1]=min(dp[t+1][j+1],dp[t][j]+abs(t+1-al[j]))
    ans=10**10
    for t in range(MAX_T):
        ans=min(ans,dp[t][n])
    ansl.append(ans)
for ans in ansl:print(ans) 