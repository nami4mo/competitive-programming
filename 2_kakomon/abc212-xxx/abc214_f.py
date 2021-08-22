s=input()
n=len(s)

dp=[0]*(n+1)
dp[0]=1
dp[1]=1

MOD=10**9+7
for i in range(1,n):
    ind=-1
    for j in range(i-1,-1,-1):
        if s[j]==s[i]:
            ind=j
            break

    if ind==-1:
        for j in range(0,i):
            dp[i+1]+=dp[j]
            dp[i+1]%=MOD  
    else:
        ind=max(1,ind)
        for j in range(ind,i):
            dp[i+1]+=dp[j]
            dp[i+1]%=MOD

ans=sum(dp)-1
print(ans%MOD)