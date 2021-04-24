n=int(input())
al=[int(input()) for _ in range(n)]

ans=1
c=0
ci=0
MOD=10**9+7
for i in range(n):
    c+=pow(10,ci)*al[i]
    if c<pow(10,ci+1):
        ans*=(c+1)
        ans%=MOD
        c=0
        ci=0
    else:
        ci+=1
ans*=(c+1)
ans-=1
print(ans%MOD)