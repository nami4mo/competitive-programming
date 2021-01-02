n=int(input())
al=list(map(int, input().split()))
MAX=10001
dp=[False]*MAX
dp[0]=True
for a in al:
    new_dp=dp[:]
    for i in range(MAX):
        if a+i<MAX and dp[i]:
            new_dp[a+i]=True
    dp=new_dp[:]
ans=0
for d in dp:
    if d:ans+=1
print(ans)