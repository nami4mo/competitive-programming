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


n = int(input())
xl = list(map(int, input().split()))
com = Combination(10**5+1)
MOD = 10**9+7

# print(com.perm(0,0),com.perm(1,1))

csum = 0
ans = 0
for i in range(n-1):
    diff = xl[i+1]-xl[i]
    val = com.com(n-1,i+1)*com.perm(i,i)*com.perm(n-2-i,n-2-i)
    # print(val,'-')
    csum += val
    csum %= MOD
    ans += diff*csum
    ans %= MOD

print(ans)