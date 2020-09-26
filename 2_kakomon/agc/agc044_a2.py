ansl = []
for _ in range(int(input())):
    n,a,b,c,d = map(int, input().split())
    INF = 10**30
    # dp = [INF]*(n+1)
    dp = {}
    dp[n] = 0

    for i in range(n,1,-1):
        
        if i%2 == 0: dp[i//2] = min(dp[i//2], dp[i]+a)
        if i%3 == 0: dp[i//3] = min(dp[i//3], dp[i]+b)
        if i%5 == 0: dp[i//5] = min(dp[i//5], dp[i]+c)

        if i >= 1: dp[i-1] = min(dp[i-1], dp[i]+d)
        if i >= 2: dp[i-2] = min(dp[i-2], dp[i]+d*2)
        if i >= 3: dp[i-3] = min(dp[i-3], dp[i]+d*3)
        if i >= 4: dp[i-4] = min(dp[i-4], dp[i]+d*4)

        if i >= 1: dp[i-1] = min(dp[i-1], dp[i]+d)
        if i >= 2: dp[i-2] = min(dp[i-2], dp[i]+d*2)
        if i >= 3: dp[i-3] = min(dp[i-3], dp[i]+d*3)
        if i >= 4: dp[i-4] = min(dp[i-4], dp[i]+d*4)

        dp[0] = min(dp[0], dp[i]+i*d)

    ansl.append(dp[0])

for a in ansl: print(a)
