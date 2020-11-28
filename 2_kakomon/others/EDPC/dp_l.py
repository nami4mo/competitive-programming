# TLE

import sys
sys.setrecursionlimit(10**6)
INF = 10**18
def rec(dp,l,r,n,al):
    if r-l == 0: return 0
    if dp[l][r] != INF:
        return dp[l][r] 
    rem = r-l
    if (n-rem)%2 == 0: # first
        if r-l == 1:
            dp[l][r] = al[l]
            return dp[l][r]
        v1 = rec(dp,l+1,r,n,al)+al[l]
        v2 = rec(dp,l,r-1,n,al)+al[r-1]
        dp[l][r] = max(v1,v2)
        return dp[l][r]

    else: # second
        if r-l == 1:
            dp[l][r] = -al[l]
            return dp[l][r]
        v1 = rec(dp,l+1,r,n,al)-al[l]
        v2 = rec(dp,l,r-1,n,al)-al[r-1]
        dp[l][r] = min(v1,v2)
        return dp[l][r]

n = int(input())
al = list(map(int, input().split()))
dp = [ [INF]*(n+1) for _ in range(n)]
ans = rec(dp,0,n,n,al)
print(ans)