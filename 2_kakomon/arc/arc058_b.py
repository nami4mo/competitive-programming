
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
# comb.com(10,3)


h,w,a,b = map(int, input().split())
minhw = min(h-a,w-b)

ans = 0
start = (h-a,b+1)
for i in range(minhw):
    hmove1 = start[0]-i -1
    wmove1 = start[1]+i -1
    c1 = comb.com(hmove1+wmove1,hmove1)

    hmove2 = h -(start[0]-i)
    wmove2 = w -(start[1]+i)
    c2 = comb.com(hmove2+wmove2,hmove2)
    ans += c1*c2
    ans %= MOD

print(ans)