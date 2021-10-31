n,p=map(int, input().split())
MOD=10**9+7
ans=p-1
ans*=pow(p-2,n-1,MOD)
print(ans%MOD)