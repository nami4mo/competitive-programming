n=int(input())
s=input()
dp=[[0]*8 for _ in range(n+1)]
dp[0][1]=1

MOD=10007
d={'J':0,'O':1,'I':2}
for i in range(n):
    si=s[i]
    bit1=(1<<d[si])
    for j in range(8):
        if bit1&j==0:continue
        for k in range(8):
            if j&k: dp[i+1][j]+=dp[i][k]
        dp[i+1][j]%=MOD

# print(dp)
ans=sum(dp[-1])%MOD
print(ans)