n=int(input())
al=list(map(int, input().split()))
al=[(a,i) for i,a in enumerate(al)]
al.sort(reverse=True)

dp=[[0]*(n+1) for _ in range(n+1)]
for num, (a,i) in enumerate(al):
    for l in range(num+1):
        r=num-l
        dp[l+1][r]=max(dp[l+1][r], dp[l][r]+abs(i-l)*a)
        dp[l][r+1]=max(dp[l][r+1], dp[l][r]+abs(n-1-r-i)*a)

ans=0
for i in range(n):
    ans=max(ans, dp[i][n-i])
print(ans)