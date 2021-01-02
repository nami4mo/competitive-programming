n,m = map(int, input().split())
INF = 10**18
# dp = [ [INF] for _ in range(2**n)]
dp = [INF]*(2**n)
dp[0]=0
for _ in range(m):
    s,c = map(str, input().split())
    c=int(c)
    sv = 0
    for i, si in enumerate(s):
        if si=='Y': sv += 2**i
    for i in range(2**n):
        dp[i|sv] = min(dp[i|sv], dp[i]+c)

ans = dp[2**n-1]
if ans == INF:ans=-1
print(ans)