n,s = map(int, input().split())
al = list(map(int, input().split()))

MOD = 998244353
dp = [ [0]*(s+1) for _ in range(n+1)]
dp[0][0] = 1
ans = 0
for i,a in enumerate(al):
    right = n-i
    if a <= s:
        dp[i+1][a] += (i+1)
    if a == s:
        ans += (i+1)*right

    for j in range(1,s+1):
        dp[i+1][j] += dp[i][j]
        if j+a <= s:
            dp[i+1][j+a] += dp[i][j]
            dp[i+1][j+a]%=MOD
        if j+a == s:
            # print(i,j,a)
            ans += dp[i][j]*right
            # print(dp[i][j]*pattern)
            ans%=MOD

# print(dp[n])
print(ans)