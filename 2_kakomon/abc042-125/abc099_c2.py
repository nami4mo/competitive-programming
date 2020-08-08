n = int(input())
dp = [200000] * (n+10)
dp[0] = 0
for i in range(1,n+1):
    dp[i] = min(dp[i-1]+1, dp[i])
    
    six = 6
    while i - six >= 0:
        dp[i] = min(dp[i-six]+1, dp[i])
        six *= 6 

    nine = 9
    while i - nine >= 0:
        dp[i] = min(dp[i-nine]+1, dp[i])
        nine *= 9

print(dp[n])