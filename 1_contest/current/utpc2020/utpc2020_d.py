def modinv(a,m,d):
    if a in d:return d[a]
    b, u, v = m, 1, 0
    while b:
        t = a//b
        a -= t*b
        a,b = b,a
        u -= t * v
        u,v = v,u
    u %= m
    return u
    
class Combination:
    def __init__(self, n_max=10**6, mod=10**9+7):
        # self._n_max = n_max
        self._fac, self._finv, self._inv = [0]*n_max, [0]*n_max, [0]*n_max
        self._fac[0], self._fac[1] = 1, 1
        self._finv[0], self._finv[1] = 1, 1
        self._inv[1] = 1
        self._mod = mod
        for i in range(2, n_max):
            self._fac[i] = self._fac[i - 1] * i % self._mod
            self._inv[i] = self._mod - self._inv[self._mod%i] * (self._mod // i) % self._mod
            self._finv[i] = self._finv[i - 1] * self._inv[i] % self._mod
    def com(self, n, r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self._fac[n] * (self._finv[r] * self._finv[n - r] % self._mod) % self._mod

    def perm(self,n,r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self._fac[n] * (self._finv[n-r] % self._mod) % self._mod
MOD=998244353
comb = Combination(10**5, MOD)
# comb.com(10,3)

d={}
n,k=map(int, input().split())
ml=list(map(int, input().split()))
ml.sort(reverse=True)

sdp=[[0]*(n+1) for _ in range(n+1)]
dp=[[0]*(n+1) for _ in range(n+1)]
maxm={}

for i in range(1,n+1):
    dp[1][i]=ml[i-1]
    sdp[1][i]=sdp[1][i-1]+ml[i-1]
    m=ml[i-1]
    maxm.setdefault(m,0)
    maxm[m]=i

# print(dp)
# print(sdp)
for k in range(2,n+1):
    for i in range(k,n+1):

        m=modinv(m,MOD,d)
        dp[k][i]=(sdp[k-1][i-1]*m)%MOD
        sdp[k][i]=(sdp[k][i-1]+dp[k][i])%MOD
print(dp)
print(sdp)

mst=set(ml)
mstl=list(mst)
mstl.sort(reverse=True)
mstl.append(0)
ans=0
for i in range(len(mstl)-1):
    m=mstl[i]
    dist=mstl[i]-mstl[i-1]
    comval=sdp[k][maxm[m]]*dist
    # comval%=MOD
    ans+=comval
    ans%=MOD

ans*=modinv(comb.com(n,k),MOD,d)
print(ans)

# ans=modinv(comval)
# for mi in 