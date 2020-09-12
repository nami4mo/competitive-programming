n = int(input())
al = list(map(int, input().split()))

dp = [10**10]*(n)
dp[0] = 0

for i in range(n):
    if i+2 < n:
        dp[i+2] = min(dp[i]+abs(al[i+2]-al[i]), dp[i+2])
    if i+1 < n:
        dp[i+1] = min(dp[i]+abs(al[i+1]-al[i]), dp[i+1])

print(dp[n-1])