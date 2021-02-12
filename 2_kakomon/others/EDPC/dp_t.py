n=int(input())
s=input()

dp=[[0]*n for _ in range(n)]
for i in range(n):
    dp[0][i]=1

MOD=10**9+7
for i in range(n-1):
    sdp=[0]
    for j in range(n):
        v=sdp[-1]+dp[i][j]
        sdp.append(v%MOD)
    if s[i]=='<':
        for j in range(n-i-1):
            dp[i+1][j]=(sdp[n]-sdp[j+1])%MOD
    else:
        for j in range(n-i-1):
            dp[i+1][j]=sdp[j+1]

# print(dp)
print(dp[-1][0])