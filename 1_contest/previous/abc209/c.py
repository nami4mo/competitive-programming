n=int(input())
al=list(map(int, input().split()))
MOD=10**9+7
al.sort()
ans=1
for i in range(n):
    v=al[i]-i
    if v<=0:ans=0
    ans*=v
    ans%=MOD
print(ans)