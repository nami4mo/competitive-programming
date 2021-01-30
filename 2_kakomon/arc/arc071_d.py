n=int(input())

if n==1:
    print(1)
    exit()
if n==2:
    print(4)
    exit()

dp=[0]*(n+1)
sdp=[0]*(n+1)

dp[0]=1
dp[1]=n
dp[2]=n**2

sdp[0]=1
sdp[1]=n+1
sdp[2]=n**2+n+1

MOD=10**9+7
for i in range(2,n):
    dp[i+1]=sdp[i]-dp[i-1]+(n-1)**2+dp[0]*(n-i)
    dp[i+1]%=MOD
    sdp[i+1]=sdp[i]+dp[i+1]
    sdp[i+1]%=MOD

print(dp[n])