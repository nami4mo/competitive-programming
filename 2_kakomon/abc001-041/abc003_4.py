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
comb = Combination(10**4, MOD)
# comb.com(10,3)

r,c = map(int, input().split())
x,y = map(int, input().split())
d,l = map(int, input().split())
xy = x*y
dl = d+l

x_pattern = r-x+1
y_pattern = c-y+1
xy_comb = x_pattern*y_pattern

if xy == dl:
    xy_dl = 1
else:
    one = comb.com(xy-x,dl)*2 + comb.com(xy-y,dl)*2
    two = comb.com(xy-x-y+1,dl)*4 + comb.com(xy-2*x,dl) + comb.com(xy-2*y,dl)
    three = comb.com(xy-2*x-y+2,dl)*2 + comb.com(xy-x-2*y+2,dl)*2
    four = comb.com(xy-2*x-2*y+4, dl)
    not_xy_dl = one - two + three - four
    xy_dl = comb.com(xy, dl) - not_xy_dl
    xy_dl%=MOD

ans = xy_comb * xy_dl * comb.com(dl, d)
print(ans%MOD)