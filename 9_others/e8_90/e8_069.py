n,k=map(int, input().split())
if n==1:
    print(k)
elif n==2:
    print(k*(k-1))
else:
    MOD=10**9+7
    ans=k*(k-1)*pow(k-2,n-2,MOD)
    ans%=MOD
    print(ans)