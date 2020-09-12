class Combination:
    def __init__(self, n_max=10**6, mod=10**9+7):
        # self._n_max = n_max
        self._fac, self._finv, self._inv = [0]*n_max, [0]*n_max, [0]*n_max
        self._fac[0], self._fac[1] = 1, 1
        self._finv[0], self._finv[1] = 1, 1
        self._inv[1] = 1
        for i in range(2, n_max):
            self._fac[i] = self._fac[i - 1] * i % MOD
            self._inv[i] = MOD - self._inv[MOD%i] * (MOD // i) % MOD
            self._finv[i] = self._finv[i - 1] * self._inv[i] % MOD
    def com(self, n, r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self._fac[n] * (self._finv[r] * self._finv[n - r] % MOD) % MOD


MOD = 10**9+7
# comb.com(10,3)
comb = Combination(10**5+1, MOD)
n,k = map(int, input().split())
al=list(map(int, input().split()))  
al.sort(reverse=True)

fmax = 0
for i,a in enumerate(al):
    cnt = comb.com(n-i-1,k-1)
    fmax += cnt*a
    fmax%=MOD

al.sort()
fmin = 0
for i,a in enumerate(al):
    cnt = comb.com(n-i-1,k-1)
    fmin += cnt*a
    fmin%=MOD

ans = fmax-fmin
ans%=MOD
print(ans)