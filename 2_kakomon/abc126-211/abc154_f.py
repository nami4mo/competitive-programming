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

n = 2*(10**6)+100
# n = 100
MOD = 10**9+7
comb = Combination(n, MOD)

r1,c1,r2,c2 = map(int, input().split())

curr_r2 = 0
r2top = 0
r2bottom = 0
for i in range(c2+1):
    curr_r2 += comb.com(r2+i+1,i+1)
    curr_r2 %= MOD
    if i+1 == c1:
        r2bottom = curr_r2
r2top = curr_r2

r1-=1
curr_r1 = 0
r1top = 0
r1bottom = 0
for i in range(c2+1):
    curr_r1 += comb.com(r1+i+1,i+1)
    curr_r1 %= MOD
    if i+1 == c1:
        r1bottom = curr_r1
r1top = curr_r1

ans = r2top - r1top - r2bottom + r1bottom
print(ans%MOD)
# print(r2top,r1top,r2bottom,r1bottom)