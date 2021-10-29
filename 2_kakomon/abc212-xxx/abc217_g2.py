'''
包除原理
'''

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

    def lucas(self, n, r): # nCr (mod self._mod(prime)) 
        if n < r: return 0 
        res = 1
        while n > 0:
            nq, rq = n//self._mod, r//self._mod
            nr, rr = n-nq*self._mod, r-rq*self._mod
            res *= self.com(nr, rr)
            res %= self._mod
            n, r = nq, rq
        return res

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

MOD = 998244353
comb = Combination(10**6, MOD)

n,m=map(int, input().split())
cnts=[0]*m
for i in range(1,n+1):
    cnts[i%m]+=1

csum=0
res=[-1]*(n+1)
for k in range(1,n+1):
    val=1
    for i in range(m):
        val*=comb.perm(k,cnts[i])
        val%=MOD
    res[k]=val

for k in range(1,n+1):
    val=0
    for j in range(1,n+1):
        if (k-j)%2==1: val-=res[j]*comb.com(k,j)
        else: val+=res[j]*comb.com(k,j)
        val%=MOD
    val*=modinv(comb.perm(k,k),MOD)
    val%=MOD
    print(val)
        
