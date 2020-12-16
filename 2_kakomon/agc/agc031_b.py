n=int(input())
dp=[0]*(2*(10**5))
MOD=10**9+7
prev=1
prev_c=-1
ans=1
for _ in range(n):
    c=int(input())-1
    if c==prev_c:continue

    ans=prev
    ans+=dp[c]
    ans%=MOD

    dp[c]=ans
    prev=ans
    prev_c=c


print(ans%MOD)