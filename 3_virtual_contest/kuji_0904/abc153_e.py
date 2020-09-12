h,n = map(int, input().split())
abl = [tuple(map(int, input().split())) for _ in range(n)]

dp = [10**18]*(h+1)
dp[0] = 0
for i in range(h):
    for a,b in abl:
        next_h = min(h,i+a)
        dp[next_h] = min(dp[next_h], dp[i]+b)

print(dp[-1])