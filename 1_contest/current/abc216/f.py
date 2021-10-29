n=int(input())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))

ail=[(a,i) for i,a in enumerate(al)]
ail.sort(reverse=False)
al.sort(reverse=False)

new_bl=[]
for a,i in ail:
    new_bl.append(bl[i])
bl=new_bl

ans=0
MOD=998244353
MAX=al[-1]+1
dp=[[0]*(MAX) for _ in range(n+1)]
dp[0][0]=1
for i in range(n):
    a=al[i]
    b=bl[i]
    for j in range(a+1-b):
        ans+=dp[i][j]
        ans%=MOD
    for j in range(MAX):
        dp[i+1][j]+=dp[i][j]
        dp[i+1][j]%=MOD
        if j+b<MAX:
            dp[i+1][j+b]+=dp[i][j]
            dp[i+1][j+b]%=MOD
    # print('--',i,ans)
print(ans)
# print(dp)