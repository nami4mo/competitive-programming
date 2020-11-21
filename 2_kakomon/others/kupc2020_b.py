from bisect import bisect_left, bisect_right

n,k = map(int, input().split())
vl = [list(map(int, input().split())) for _ in range(n)]
MOD = 10**9+7
dp = [ [0]*k for _ in range(n) ]
for j in range(k):
    dp[0][j] = 1

for i in range(1,n):
    cdp = []
    v = 0
    for j in range(k):
        v += dp[i-1][j]
        cdp.append(v)
    
    for j in range(k):
        ind = bisect_right(vl[i-1], vl[i][j]) - 1
        if ind < 0: continue
        dp[i][j] = cdp[ind]

ans = sum(dp[n-1])%MOD
print(ans)