n = int(input())
dp = [200000] * (n+10)
dp[0] = 0
for i in range(n):
    dp[i+1] = min(dp[i+1], dp[i]+1)
    six = 6
    while i + six <= n:
        dp[i+six] = min(dp[i+six], dp[i]+1)
        six *= 6 

    nine = 9
    while i + nine <= n:
        dp[i+nine] = min(dp[i+nine], dp[i]+1)
        nine *= 9

print(dp[n])