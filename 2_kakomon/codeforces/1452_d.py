def modinv(a,m):
    b, u, v = m, 1, 0
    while b:
        t = a//b
        a -= t*b
        a,b = b,a
        u -= t * v
        u,v = v,u
    u %= m
    return u

n=int(input())
dp=[0]*(n+1)
sdp0=[0,1]
sdp1=[0,1]
dp[0]=1
dp[1]=1
MOD=998244353
for i in range(2,n+1):
    if i%2==0:
        dp[i]=sdp1[i//2]%MOD
        sdp0.append((dp[i]+sdp0[-1])%MOD)
    else:
        dp[i]=sdp0[i//2+1]%MOD
        sdp1.append((dp[i]+sdp1[-1])%MOD)
# print(dp)

x=dp[n]
y=pow(2,n,MOD)
ans=x*modinv(y,MOD)
print(ans%MOD)