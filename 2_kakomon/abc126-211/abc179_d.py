n,k = map(int, input().split())

lrs = []
for _ in range(k):
    l,r = map(int, input().split())
    lrs.append((l,r))

dp = [0]*(n+1)
sdp = [0]*(n+1)
dp[1] = 1
sdp[1] = 1

MOD = 998244353
for i in range(2,n+1):
    # print('------',i)
    for l,r in lrs:
        dr = sdp[i-l] if i-l >= 0 else 0
        dl = sdp[i-r-1] if i-r-1 >= 0 else 0
        # print(dl,dr,'--')
        dp[i] += (dr-dl)
        dp[i] %= MOD        
    sdp[i] = sdp[i-1] + dp[i]
    sdp[i]%=MOD

# print(dp)
print(dp[n])