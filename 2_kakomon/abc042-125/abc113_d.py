MOD = 10**9+7
h,w,k = map(int, input().split())

patterns = [1,1,2,3,5,8,13,21]

dp = [ [0]*w for _ in range(h+1) ]
dp[0][0] = 1
for i in range(1,h+1):
    for wi in range(w):
        dp[i][wi] = dp[i-1][wi] * patterns[w-1-wi] * patterns[wi-0]
        if wi > 0:
            dp[i][wi] += dp[i-1][wi-1] * patterns[w-1-wi] * patterns[wi-1]
        if wi < w-1:
            dp[i][wi] += dp[i-1][wi+1] * patterns[w-1-wi-1] * patterns[wi-0]
        dp[i][wi] %= MOD

print(dp[h][k-1]%MOD)