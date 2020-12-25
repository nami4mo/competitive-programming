from bisect import bisect_left
INF = 10**10

n = int(input())
dp=[0]*(n+1)

for _ in range(n):
    a=int(input())
    dp[a]=dp[a-1]+1

print(n-max(dp))