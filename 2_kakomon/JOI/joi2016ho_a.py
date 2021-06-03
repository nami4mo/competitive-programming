n,m,k=map(int, input().split())
al=[int(input()) for _ in range(n)]

dp=[10**18]*(n+1)
dp[0]=0
for i in range(n):
    ma,mi=al[i],al[i]
    for j in range(1,m+1):
        if i+j-1>=n:break
        ma=max(ma, al[i+j-1])
        mi=min(mi, al[i+j-1])
        dp[i+j]=min(dp[i+j], dp[i]+k+(ma-mi)*j)

print(dp[n])