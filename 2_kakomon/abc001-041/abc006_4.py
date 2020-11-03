from bisect import bisect_left

n = int(input())
al = []
for _ in range(n):
    a = int(input())
    al.append(a)

INF = 10**10
dp = [INF]*(n+1)
dp[0] = -INF

for i, a in enumerate(al):
    ind = bisect_left(dp, a) # max index of "value <= a"
    dp[ind] = a
ans = bisect_left(dp, INF) - 1 # cnt of "value < INF" and remove 0-index
print(n-ans)