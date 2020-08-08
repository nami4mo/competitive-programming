n = int(input())

dp = [ {ch: {'a':0, 'c':0, 'g':0, 't':0 } for ch in ['a','c','g','t']} for _ in range(n)]
a,c,g,t = 'a','c','g','t'

for ch1 in [a,c,g,t]:
    for ch2 in [a,c,g,t]:
        dp[1][ch1][ch2] = 1

for i in range(1,n-1):
    dp[i+1][a][a] = dp[i][a][a] + dp[i][c][a] + dp[i][g][a] + dp[i][t][a]
    dp[i+1][c][a] = dp[i][a][c] + dp[i][c][c] + dp[i][g][c] + dp[i][t][c]
    dp[i+1][g][a] = dp[i][a][g] + dp[i][c][g] + dp[i][g][g] + dp[i][t][g]
    dp[i+1][t][a] = dp[i][a][t] + dp[i][c][t] + dp[i][g][t] + dp[i][t][t]

    dp[i+1][a][c] = dp[i][a][a] + dp[i][c][a] + dp[i][g][a]*0 + dp[i][t][a]
    dp[i+1][c][c] = dp[i][a][c] + dp[i][c][c] + dp[i][g][c] + dp[i][t][c]
    dp[i+1][g][c] = dp[i][a][g]*0 + dp[i][c][g] + dp[i][g][g] + dp[i][t][g]
    dp[i+1][t][c] = dp[i][a][t] + dp[i][c][t] + dp[i][g][t] + dp[i][t][t]

    dp[i+1][a][g] = dp[i][a][a] + dp[i][c][a] + dp[i][g][a] + dp[i][t][a]
    dp[i+1][c][g] = dp[i][a][c]*0 + dp[i][c][c] + dp[i][g][c] + dp[i][t][c]
    dp[i+1][g][g] = dp[i][a][g] + dp[i][c][g] + dp[i][g][g] + dp[i][t][g]
    dp[i+1][t][g] = dp[i][a][t] + dp[i][c][t] + dp[i][g][t] + dp[i][t][t]

    dp[i+1][a][t] = dp[i][a][a] + dp[i][c][a] + dp[i][g][a] + dp[i][t][a]
    dp[i+1][c][t] = dp[i][a][c] + dp[i][c][c] + dp[i][g][c] + dp[i][t][c]
    dp[i+1][g][t] = dp[i][a][g] + dp[i][c][g] + dp[i][g][g] + dp[i][t][g]
    dp[i+1][t][t] = dp[i][a][t] + dp[i][c][t] + dp[i][g][t] + dp[i][t][t]

ans = 0
for ch1 in [a,c,g,t]:
    for ch2 in [a,c,g,t]:
        ans += dp[n-1][ch1][ch2]

# print(dp)
print(ans%(10**9+7))