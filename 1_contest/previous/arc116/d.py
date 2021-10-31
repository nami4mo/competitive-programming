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

MOD = 998244353
comb = Combination(5*10**3+1, MOD)
comb.com(10,3)

n,m=map(int, input().split())
dp=[[0]*(m+1) for _ in range(16)]

dp[0][0]=1

for i in range(0,15):
    bitval=pow(2,i)
    # print('---',i)
    for cnt in range(0,n+1,2):
        bsum=bitval*cnt
        pat=comb.com(n,cnt)
        # print(bsum,pat)
        for j in range(m+1):
            if j+bsum>m:break
            dp[i+1][j+bsum]+=dp[i][j]*pat
            dp[i+1][j+bsum]%=MOD

# print(dp[:6])
ans=dp[-1][m]
print(ans)