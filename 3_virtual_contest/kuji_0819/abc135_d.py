s = input()
n = len(s)

MOD = 10**9+7
dp = [ [0]*13 for _ in range(n+1) ]
dp[0][0] = 1
for i in range(n):
    si = s[i]
    if si == '?':
        for j in range(13):
            for k in range(10):
                dp[i+1][(j*10+k)%13] += dp[i][j]
                dp[i+1][(j*10+k)%13]%=MOD

    else:
        sii = int(si)
        for j in range(13):
            dp[i+1][(j*10+sii)%13] += dp[i][j]
            dp[i+1][(j*10+sii)%13]%=MOD


print(dp[n][5])