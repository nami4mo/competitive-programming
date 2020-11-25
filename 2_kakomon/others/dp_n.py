# TLE

import sys
sys.setrecursionlimit(10**6)

INF = 10**18
def rec(l,r,dp,cumsums):
    if l == r-1:
        return 0
        # dp[l][r] = cumsums[r]
        # return dp[l][r]
    if l > r-1:
        return 0
    if dp[l][r] != 0:
        return dp[l][r]

    v = cumsums[r]-cumsums[l]
    min_v = INF
    for i in range(l+1,r):
        v2 = rec(l,i,dp,cumsums)+rec(i,r,dp,cumsums)
        min_v = min(min_v,v2) 
    dp[l][r] = v+min_v
    return v+min_v

n = int(input())
al = list(map(int, input().split()))
dp = [[0]*(n+1) for _ in range(n+1)]

cumsums = [0]
c = 0
for a in al:
    c+=a
    cumsums.append(c)

ans = rec(0,n,dp,cumsums)
# print(dp)
print(ans)