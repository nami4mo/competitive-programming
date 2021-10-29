n=int(input())
ans=0
MOD=998244353
for i in range(1,10**6+10):
    start=i**2
    step=i*2
    if start>n:break
    cnt=(n-start)//step+1
    ans+=cnt
    ans%=MOD
print(ans)