n,k=map(int, input().split())
al=[0]*(k+1)

MOD=10**9+7
for i in range(k,0,-1):
    cnt=k//i
    pat=pow(cnt,n,MOD)
    for j in range(i+i,k+1,i):
        pat-=al[j]
    al[i]=pat%MOD

ans=0
for i in range(k+1):
    ans+=i*al[i]
    ans%=MOD
print(ans)