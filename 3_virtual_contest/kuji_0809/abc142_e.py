n,m = map(int, input().split())
# abl = []
# cl = []

dp = [ [10**9]*(2**n) for _ in range(m+1) ]
dp[0][0] = 0
for i in range(m):
    a,b = map(int, input().split())
    cl = list(map(int, input().split()))
    cbit = 0
    for c in cl:
        cbit += 2**(c-1)
    
    for j in range(2**n):
        if dp[i][j] == 10**9:
            continue
        dp[i+1][j] = min(dp[i][j], dp[i+1][j])
        dp[i+1][j|cbit] = min(dp[i][j]+a, dp[i][j|cbit], dp[i+1][j|cbit])

ans = dp[m][2**n-1]
if ans >= 10**9:
    ans = -1

print(ans)