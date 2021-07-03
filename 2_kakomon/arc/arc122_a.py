n=int(input())
al=list(map(int, input().split()))

MOD=10**9+7
ans=0

oks=[-1]*n
oks=[1,2,3]
for i in range(n):
    oks.append((oks[-1]+oks[-2])%MOD)

def get_oks(i):
    if i<0:return 1
    else: return oks[i]

# print(oks)
c=0
for i in range(n-1):
    a=al[i+1]
    lc=i
    rc=n-2-i
    pc=oks[lc]*oks[rc]
    mc=get_oks(lc-1)*get_oks(rc-1)
    val=a*(pc-mc)
    ans+=val
    ans%=MOD

ans+=al[0]*oks[n-1]
ans%=MOD

print(ans)