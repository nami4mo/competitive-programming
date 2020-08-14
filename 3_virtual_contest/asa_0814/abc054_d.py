n,ma,mb = map(int, input().split())
abcl = []
for _ in range(n):
    a,b,c = map(int, input().split())
    abcl.append((a,b,c))

dp = [ [ [10**9]*401  for _ in range(401) ] for _ in range(n+1) ]
dp[0][0][0] = 0
for i in range(n):
    ai,bi,ci = abcl[i]
    for a in range(401):
        for b in range(401):
            if a+ai < 401 and b+bi < 401:
                dp[i+1][a][b] = min(dp[i][a][b], dp[i+1][a][b])
                dp[i+1][a+ai][b+bi] = min(dp[i][a][b] + ci, dp[i+1][a+ai][b+bi])


ans = 10**9
dp_row = dp[n]
for a in range(1,401):
    for b in range(1,401):
        if ma*b == mb*a:
            v = dp[n][a][b]
            ans = min(ans,v)

if ans == 10**9: ans = -1
print(ans)