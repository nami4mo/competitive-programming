n=int(input())
dp=[-1]*(n+1)
dp[1]=0
for i in range(1,n):
    dp[i+1]=dp[i]+(n/(n-i))
print(dp[n])