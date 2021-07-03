n,d=map(int, input().split())
al=list(map(int, input().split()))
dp=[[0]*(1<<n) for _ in range(d+1)]
dp[0][0]=1
for i in range(d):
    bits=0
    for j in range(n):
        if al[j]&(1<<i): bits|=(1<<j)
    for j in range(1<<n):
        dp[i+1][j]+=dp[i][j]
        dp[i+1][j|bits]+=dp[i][j]
print(dp[d][-1])