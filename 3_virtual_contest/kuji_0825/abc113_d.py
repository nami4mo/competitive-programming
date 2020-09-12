h,w,k = map(int, input().split())
remv = [1,1,2,3,5,8,13,21]

dp = [ [0]*w for _ in range(h+1) ]
dp[0][0] = 1

MOD = 10**9+7
for i in range(h):
    for wi in range(w):
        left = wi
        right = w-wi-1
        com = remv[left] * remv[right]
        dp[i+1][wi] += dp[i][wi]*com
        dp[i+1][wi] %= MOD

        if wi > 0:
            left = wi-1
            right = w-wi-1
            com = remv[left] * remv[right]
            dp[i+1][wi-1] += dp[i][wi]*com
            dp[i+1][wi-1] %= MOD

        if wi < w-1:
            left = wi
            right = w-(wi+1)-1
            com = remv[left] * remv[right]
            dp[i+1][wi+1] += dp[i][wi]*com
            dp[i+1][wi+1] %= MOD


print(dp[h][k-1])

