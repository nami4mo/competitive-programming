
MOD = 10**9+7
s = input()
n = len(s)
dp = [ [0]*13 for _ in range(n+1) ]
dp[0][0] = 1

for i in range(n):
    if s[i] == '?':
        for j in range(13):
            for num in range(0,9+1):
                dp[i+1][(j*10+num)%13] += dp[i][j]
                dp[i+1][(j*10+num)%13]%=MOD
    else:
        num = int(s[i])
        for j in range(13):
            dp[i+1][(j*10+num)%13] += dp[i][j]
            dp[i+1][(j*10+num)%13]%=MOD

print(dp[n][5])