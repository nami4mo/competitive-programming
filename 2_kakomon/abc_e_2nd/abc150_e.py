n=int(input())
cl=list(map(int, input().split()))
cl.sort(reverse=True)

ans=0
MOD=10**9+7
for i,c in enumerate(cl):
    if i==0:
        ans+=(c*pow(2,n-1,MOD))
    else:
        mul=pow(2,n-i-1,MOD)
        v=pow(2,i,MOD)+i*pow(2,i-1,MOD)
        ans+=(mul*v*c)
        ans%=MOD

ans*=pow(2,n,MOD)
print(ans%MOD)