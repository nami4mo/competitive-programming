n=int(input())
al=[]
for _ in range(n):
    al.append(list(map(int, input().split())))

dp=[0]*(2**n)
dp[0]=1
MOD=10**9+7
for i in range(1,2**n):
    popcount=bin(i).count("1")
    man_i=popcount
    for j in range(n): # i-th man / j-th woman
        if (i>>j)%2==0:continue
        if al[man_i-1][j]==1:
            dp[i]+=dp[i-2**j]
            dp[i]%=MOD
print(dp[-1])