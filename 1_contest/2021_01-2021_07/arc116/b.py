n=int(input())
al=list(map(int, input().split()))
al.sort()

MOD=998244353
ans=0
csum=0
asum=0
for i in range(n-2,-1,-1):
    # asum+=al[i+1]
    # # csum+=asum
    csum=(csum*2)+al[i+1]
    csum%=MOD
    v=al[i]*csum
    ans+=v
    ans%=MOD

for i in range(n):
    ans+=(al[i]**2)
    ans%=MOD
print(ans)
