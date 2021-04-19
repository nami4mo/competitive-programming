n=int(input())
al=list(map(int, input().split()))
al=[0]+al
al.sort()
ans=1
MOD=10**9+7
for i in range(n):
    d=al[i+1]-al[i]+1
    ans*=d
    ans%=MOD
print(ans)