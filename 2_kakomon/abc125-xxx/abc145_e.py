N,T = map(int, input().split())
abl = []
for _ in range(N):
    a,b = map(int, input().split())
    abl.append((a,b))

abl.sort()
dp = [ [0]*6001 for _ in range(N+1) ]

for i in range(N):
    a,b = abl[i]
    for t in range(6001):
        dp[i+1][t] = max(dp[i+1][t], dp[i][t])
        if t < T: dp[i+1][t+a] = max(dp[i][t]+b, dp[i][t+a])


ans = max(dp[N])
print(ans)