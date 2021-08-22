n=int(input())
s=input()

MOD=998244353
dp=[[0]*(1<<10) for _ in range(11)]
dp[10][0]=1
for i in range(n):
    si=s[i]
    v=ord(si)-ord('A')
    vbit=1<<v
    new_dp=[[0]*(1<<10) for _ in range(11)]
    for k in range(11):
        for j in range(1<<10):
            new_dp[k][j]+=dp[k][j] # not choose
            new_dp[k][j]%=MOD
            # if k==10:continue
            if k==v:
                new_dp[v][j|vbit]+=dp[k][j]
                new_dp[v][j|vbit]%=MOD
            elif j&vbit==0:
                new_dp[v][j|vbit]+=dp[k][j]
                new_dp[v][j|vbit]%=MOD
            
    for k in range(11):
        for j in range(1<<10):
            dp[k][j]=new_dp[k][j]
            dp[10][0]=1

ans=0
for k in range(10):
    for j in range(1<<10):
        ans+=dp[k][j]
        ans%=MOD
print(ans)