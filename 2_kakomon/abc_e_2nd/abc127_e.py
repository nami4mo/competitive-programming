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

MOD = 10**9+7
comb = Combination(10**6, MOD)

def solve(n,m,k):
    v=0
    for i in range(1,m):
        v+=i*(m-i)
        v%=MOD
    v*=(n*n)
    v*=comb.com(n*m-2,k-2)
    v%=MOD
    return v


n,m,k=map(int, input().split())
v1=solve(n,m,k)
v2=solve(m,n,k)
ans=(v1+v2)%MOD
print(ans)