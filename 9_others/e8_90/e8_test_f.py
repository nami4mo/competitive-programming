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

MOD=10**9+7
comb=Combination(5*10**5+10,MOD)

n,m=map(int, input().split())
dist=n*2
pat=comb.com(2*n,n)
ans=dist*pat
ans%=MOD

for _ in range(m):
    t,x,y=map(int, input().split())
    if t==1:
        pat1=comb.com(x+y,x)
        pat2=comb.com(2*n-(x+y+1),n-y)
        ans-=pat1*pat2
        ans%=MOD
    if t==2:
        pat1=comb.com(x+y,x)
        pat2=comb.com(2*n-(x+y+1),n-x)
        ans-=pat1*pat2
        ans%=MOD
print(ans)