n=int(input())
tl=list(map(int, input().split()))
tsum=sum(tl)
MAX=10**5+1
dp=[False]*MAX
dp[0]=True
for i in range(n):
    new_dp=[False]*MAX
    t=tl[i]
    for j in range(MAX):
        if dp[j]: new_dp[j]=True
        if dp[j] and j+t<MAX: new_dp[j+t]=True
    dp=new_dp[:]

ans=10**10
for i in range(MAX):
    if not dp[i]:continue
    rem=tsum-i
    ct=max(rem,i)
    ans=min(ans,ct)
print(ans)