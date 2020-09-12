MOD = 10**9+7
l = input()
n = len(l)

dp = [ [0]*2 for _ in range(n+1) ]
dp[0][0] = 1 # same
dp[0][1] = 0 # smaller

for i in range(n):
    if l[i] == '1':
        dp[i+1][0] = dp[i][0] * 2
        dp[i+1][1] = dp[i][0] + dp[i][1] * 3
    else:
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = dp[i][1] * 3

    dp[i+1][0]%=MOD
    dp[i+1][1]%=MOD

ans = dp[n][0] + dp[n][1]
print(ans%MOD)