H, N = map(int, input().split()) 
abl = []
for _ in range(N):
    ab = list(map(int, input().split()) )
    abl.append(ab)

dp = [10**8]*(2*10**4+1)
dp[0] = 0
for h in range(H+1):
    for ab in abl:
        a,b = ab
        dp[h+a] = min(dp[h+a], dp[h]+b)

print(min( dp[H:] ))