n,p = map(int, input().split())
abl = []
for _ in range(n):
    a,b = map(int, input().split())
    abl.append((a,b))

abl.sort(reverse=True)

p_lim = p+1+100
dp = [0] * p_lim
for i in range(n):
    a,b = abl[i]
    next_dp = [0]*p_lim
    for x in range(0,p+1+100):
        next_dp[x] = max(dp[x], next_dp[x])
        if x <= p: 
            next_dp[x+a] = max(dp[x]+b, dp[x+a])
    dp = next_dp[:]

ans = max(dp)
print(ans)