def modinv(a,m):
    b, u, v = m, 1, 0
    while b:
        t = a//b
        a -= t*b
        a,b = b,a
        u -= t * v
        u,v = v,u
    u %= m
    return u


n,k=map(int, input().split())
al=list(map(int, input().split()))
MOD=998244353

MAX=301
facs=[1]*MAX
ifacs=[1]*MAX
v=1
for i in range(1,MAX):
    v*=i
    v%=MOD
    facs[i]=v
    ifacs[i]=modinv(facs[i],MOD)
# print(facs)
# print(ifacs)

fk=[-1]*MAX
yobun=[-1]*MAX
alp=[1]*n
for i in range(MAX):
    vsum=0
    vsum2=0
    for j,a in enumerate(al):
        vsum+=alp[j]
        vsum%=MOD
        alp[j]*=a
        alp[j]%=MOD
    yobun[i]=(vsum*pow(2,i,MOD))%MOD
    vsum*=ifacs[i]
    fk[i]=vsum%MOD


d2=modinv(2,MOD)
for x in range(1,k+1):
    ans=0
    for j in range(x+1):
        ans+=fk[j]*fk[x-j]
        ans%=MOD
    ans*=facs[x]
    ans-=yobun[x]
    ans*=d2
    ans%=MOD
    print(ans)
